import functools

"""
def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper


@my_decorator
def add5(x):
    s = x + 5
    return s


# result = add5(10)
# print(result)

print(help(add5))
print(add5.__name__)
"""


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')


greet('Alex')

print(help(greet))
print(greet.__name__)
