using Next.Common.Extensions;
using StackExchange.Redis;

namespace CacheHelper;

public static class CacheHelper
{
    private static readonly IDatabase Database;
    private static readonly string KeyPrefix;

    static CacheHelper()
    {
        var redisServer = AppSettingsHelper.GetSection("Redis:Host").Value ?? "localhost";
        var redisPort = int.Parse(AppSettingsHelper.GetSection("Redis:Port").Value ?? "6379");
        var redisPassword = AppSettingsHelper.GetSection("Redis:Password").Value;
        var redisPrefix = AppSettingsHelper.GetSection("Redis:Prefix").Value ?? "nc:";

        KeyPrefix = redisPrefix;

        var redisDbConfigurationOptions = new ConfigurationOptions {
            EndPoints =
            {
                { redisServer, redisPort }
            },
            AllowAdmin = true,
            ChannelPrefix = redisPrefix
        };
        if (!string.IsNullOrWhiteSpace(redisPassword)) redisDbConfigurationOptions.Password = redisPassword;

        Database = ConnectionMultiplexer.Connect(redisDbConfigurationOptions).GetDatabase();
    }

    public static T? Get<T>(string key)
    {
        var failsafeGet = () => _get<T>(key);
        return failsafeGet.ExceptionSafeExecute();
    }

    private static T? _get<T>(string key)
    {
        key = KeyPrefix + key;
        var cacheValue = Database.StringGet(key);
        return !cacheValue.HasValue ? default : JsonHelper.Deserialize<T>(cacheValue.ToString());
    }

    public static void Set<T>(string key, T model, TimeSpan? expiration = null)
    {
        var failsafeSet = () => _set(key, model, expiration);
        failsafeSet.ExceptionSafeExecute();
    }

    private static void _set<T>(string key, T model, TimeSpan? expiration = null)
    {
        key = KeyPrefix + key;
        expiration ??= TimeSpan.FromMinutes(5);
        Database.KeyDelete(key);
        var value = JsonHelper.Serialize(model);
        Database.StringSet(key, value, expiration);
    }

    public static T? Sync<T>(string key, Func<T?> func, TimeSpan? expiration = null)
    {
        var failsafeSync = () => _sync(key, func, expiration);
        return failsafeSync.ExceptionSafeExecute();
    }

    private static T? _sync<T>(string key, Func<T?> func, TimeSpan? expiration = null)
    {
        var value = Get<T>(key);
        if (value != null) return value;
        value = func();
        if (value == null) return value;
        Set(key, value, expiration);
        return value;
    }

    public static void Remove(string key)
    {
        var failsafeRemove = () => _remove(key);
        failsafeRemove.ExceptionSafeExecute();
    }

    private static void _remove(string key)
    {
        key = KeyPrefix + key;
        Database.KeyDelete(key);
    }

    public static async Task<T?> GetAsync<T>(string key)
    {
        var failsafeGet = async () => await _getAsync<T>(key);
        return await failsafeGet.ExceptionSafeExecute();
    }

    private static async Task<T?> _getAsync<T>(string key)
    {
        key = KeyPrefix + key;
        var cacheValue = await Database.StringGetAsync(key);
        return !cacheValue.HasValue ? default : JsonHelper.Deserialize<T>(cacheValue.ToString());
    }

    public static async Task SetAsync<T>(string key, T model, TimeSpan? expiration = null)
    {
        var failsafeSet = async () => await _setAsync(key, model, expiration);
        await failsafeSet.ExceptionSafeExecute()!;
    }

    private static async Task _setAsync<T>(string key, T model, TimeSpan? expiration = null)
    {
        key = KeyPrefix + key;
        expiration ??= TimeSpan.FromMinutes(5);
        await Database.KeyDeleteAsync(key);
        var value = JsonHelper.Serialize(model);
        await Database.StringSetAsync(key, value, expiration);
    }

    public static async Task<T?> SyncAsync<T>(string key, Func<Task<T?>> func, TimeSpan? expiration = null)
    {
        var failsafeSync = async () => await _syncAsync(key, func, expiration);
        return await failsafeSync.ExceptionSafeExecute();
    }

    private static async Task<T?> _syncAsync<T>(string key, Func<Task<T?>> func, TimeSpan? expiration = null)
    {
        var value = await GetAsync<T>(key);
        if (value != null) return value;
        value = await func();
        if (value == null) return value;
        await SetAsync(key, value, expiration);
        return value;
    }

    public static async Task RemoveAsync(string key)
    {
        var failsafeRemove = async () => await _removeAsync(key);
        await failsafeRemove.ExceptionSafeExecute()!;
    }

    private static async Task _removeAsync(string key)
    {
        key = KeyPrefix + key;
        await Database.KeyDeleteAsync(key);
    }
}
