from functools import wraps


def val_checker(func):
    def checker(fun):
        @wraps(fun)
        def wraper(x):
            if func(x):
                return fun(x)
            raise ValueError from ValueError
        return wraper
    return checker



@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    #print(calc_cube('ss'))