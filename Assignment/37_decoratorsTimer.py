from functools import wraps

def timerDecorator(originalFunction):
    import time
    @wraps(originalFunction)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = originalFunction(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{originalFunction.__name__} ran in {t2}")
        return result
    return wrapper

@timerDecorator
def newFunc(num):
    for _ in range(num):
        pass

newFunc(1000)