using System.Text.Json;
using System.Text.Json.Serialization;

namespace SystemTextJsonHelper;

public static class JsonHelper
{
    private static readonly JsonSerializerOptions DefaultOptions;
    private static JsonSerializerOptions GlobalJsonSerializerOptions { get; set; }
    private static readonly object LockObject = new();


    static JsonHelper()
    {
        var defaultOption = new JsonSerializerOptions
        {
            ReferenceHandler = ReferenceHandler.IgnoreCycles,
            IncludeFields = true,
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            DictionaryKeyPolicy = JsonNamingPolicy.CamelCase,
            UnknownTypeHandling = JsonUnknownTypeHandling.JsonNode
        };
        defaultOption.Converters.Add(new JsonStringEnumConverter());

        DefaultOptions = defaultOption;
        GlobalJsonSerializerOptions = DefaultOptions;
    }

    public static void SetGlobalJsonSerializerOptions(Func<JsonSerializerOptions, JsonSerializerOptions> optionsGetter)
    {
        lock (LockObject)
        {
            GlobalJsonSerializerOptions = optionsGetter(DefaultOptions);
        }
    }

    private static JsonSerializerOptions GetDefaultOptions() => DefaultOptions;
    public static JsonSerializerOptions GetJsonSerializerOptions() => GlobalJsonSerializerOptions;

    public static string Serialize<T>(T? obj, Func<JsonSerializerOptions, JsonSerializerOptions>? optionsOverride = null)
    {
        if (optionsOverride == null) return JsonSerializer.Serialize(obj, DefaultOptions);
        var options = optionsOverride(GlobalJsonSerializerOptions);
        return JsonSerializer.Serialize(obj, options);
    }

    public static T? Deserialize<T>(string json, Func<JsonSerializerOptions, JsonSerializerOptions>? optionsOverride = null)
    {
        if (optionsOverride == null) return JsonSerializer.Deserialize<T>(json, DefaultOptions);
        var options = optionsOverride(GlobalJsonSerializerOptions);
        return JsonSerializer.Deserialize<T>(json, options);
    }
}
