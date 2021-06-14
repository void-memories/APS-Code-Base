  
from functools import wraps

def logDecorator(originalFunction):
    import logging
    logging.basicConfig(filename=f"{originalFunction.__name__}.log" , level=logging.INFO)
    
    @wraps(originalFunction)
    def wrapper(*args, **kwargs):
        logging.info(f"{originalFunction.__name__} Ran with args={args} and kwargs={kwargs}")
        return originalFunction(*args, **kwargs)
    return wrapper