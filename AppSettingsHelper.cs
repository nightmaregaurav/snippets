using System;
using Microsoft.Extensions.Configuration;
using System.IO;

namespace AppSettingsHelper
{
    public static class AppSettingsHelper
    {
        private static readonly object LockObject = new object();
        private static IConfigurationRoot? _configuration;

        private static IConfigurationRoot AllConfigurations
        {
            get
            {
                if (_configuration != null) return _configuration;

                lock (LockObject)
                {
                    if (_configuration != null) return _configuration;

                    var currentExecutionDirectory = Directory.GetCurrentDirectory();
                    var mode = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT") ?? "Development";

                    var configuration = new ConfigurationBuilder()
                        .SetBasePath(currentExecutionDirectory)
                        .AddJsonFile("appsettings.json", false, true)
                        .AddJsonFile($"appsettings.{mode}.json", true, true)
                        .AddEnvironmentVariables()
                        .Build();

                    _configuration = configuration;
                    return configuration;
                }
            }
        }

        public static IConfigurationSection GetSection(string key) => AllConfigurations.GetSection(key);
        public static IConfigurationRoot GetAllConfigurations() => AllConfigurations;
    }
}
