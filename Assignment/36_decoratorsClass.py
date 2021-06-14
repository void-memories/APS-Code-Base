class decoratorClass(object):
    def __init__(self, originalFunction):
        self.originalFunction = originalFunction

    def __call__(self, *args, **kwargs):
        print(f"Call Method executed by {self.originalFunction.__name__}")
        return self.originalFunction(*args, **kwargs)

@decoratorClass
def display(name):
    print(name)

display("Sudeep")