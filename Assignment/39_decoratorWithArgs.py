def prefixedDecorator(prefix):
    def decoratorFunction(originalFunction):
        def wrapperFunction(*args, **kwargs):
            print(f"{prefix}: Wrapper is about to run {originalFunction.__name__}")
            result = originalFunction(*args, **kwargs)
            return result
        return wrapperFunction
    return decoratorFunction

@prefixedDecorator('LOG')
def printInfo(name, age):
    print(f"{name} is {age}")

printInfo("Jon",20)