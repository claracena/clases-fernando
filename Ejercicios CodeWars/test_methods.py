from functools import wraps
from time import time

def timer(func):
    '''
    Decorator to use before any function to meassure its time complexity

    Usage:
        @timer
        def function_to_time()
        ...

    Author: Cesar Aracena (aracenameister at gmail dot com)
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_timer = time()
        result = func(*args, **kwargs)
        end_time = time()
        total = end_time - start_timer
        print(f'Function {func.__name__} took {total:.24f} seconds')
        return result
    return wrapper

if __name__ == '__main__':
    print(timer.__doc__)