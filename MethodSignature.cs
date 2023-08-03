using System;
using System.Linq;
using System.Reflection;

public class MethodSignature
{
    public string? Namespace { get; }
    public string ClassName { get;  }
    public string[] AccessModifiers { get; }
    public bool IsStatic { get; }
    public string Name { get; }
    public IList<MethodParameter> Parameters  { get; }
    public string ReturnType  { get; }

    public class MethodParameter
    {
        public string Type { get; }
        public string Name { get; }

        public MethodParameter(string type, string name)
        {
            Type = type;
            Name = name;
        }

        public new string ToString() => $"{Type} {Name}";
    }

    private MethodSignature(string? @namespace, string className, string[] accessModifiers, bool isStatic, string name, IList<MethodParameter> parameters, string returnType)
    {
        Namespace = @namespace;
        ClassName = className;
        AccessModifiers = accessModifiers;
        IsStatic = isStatic;
        Name = name;
        Parameters = parameters;
        ReturnType = returnType;
    }

    public static MethodSignature signatureof(Type classType, string methodName)
    {
        var @namespace = classType.Namespace;
        var className = classType.Name;
        var methodInfo = classType.GetMethod(methodName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static);
        if (methodInfo == null) throw new ArgumentException($"Method '{methodName}' not found in type '{classType.Name}'.");
        var visibility = GetVisibility(methodInfo);
        var isStatic = methodInfo.IsStatic;
        var parameters = methodInfo.GetParameters().Select(x => new MethodParameter(x.ParameterType.Name, x.Name ?? "anonymous")).ToList();
        var returnType = methodInfo.ReturnType.Name;

        return new MethodSignature(
            @namespace,
            className,
            visibility,
            isStatic,
            methodName,
            parameters,
            returnType
        );
    }

    private static string[] GetVisibility(MethodBase methodInfo)
    {
        if (methodInfo.IsPublic)
            return new[] {"public"};
        if (methodInfo.IsPrivate)
            return new[] {"private"};
        if (methodInfo.IsFamily)
            return new[] {"protected"};
        if (methodInfo.IsAssembly)
            return new[] {"internal"};
        if (methodInfo.IsFamilyOrAssembly)
            return new[] {"protected", "internal"};

        return methodInfo.IsFamilyAndAssembly ? new[] {"private", "protected"} : Array.Empty<string>();
    }

    public new string ToString()
    {
        return $"{string.Join(" ", AccessModifiers)} {(IsStatic ? "static " : "")} {ReturnType} {Namespace}.{ClassName}.{Name} ({string.Join(", ", Parameters.Select(x => x.ToString()))});";
    }
}
