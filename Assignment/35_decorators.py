def decoratorFunction(originalFunction):
    def wrapperFunction(*args, **kwargs):
        print("Decorator function ran")
        return originalFunction(*args, **kwargs)
    return wrapperFunction


#same as writing displayFunction = decoratorFunction(displayFunction)
@decoratorFunction
def displayFunction():
    print("Display function ran")

@decoratorFunction
def displayInfo(name, age):
    print(f"{name} is {age} years old")

displayFunction()

displayInfo("Sudeep", 20)

    