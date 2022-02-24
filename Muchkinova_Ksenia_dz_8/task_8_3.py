from functools import wraps


def type_logger(a=0):

    def logger(func):

       @wraps(func)
       def decor(*argv):
          if a > 0:
             return 'calc_cube('+", ".join([f'{func(x)}:{type(func(x))}' for x in argv]) + ")"
          else:
             return 'calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")'
       return decor
    return logger


@type_logger(2)
def calc_cube(x):
   return x ** 3


a = calc_cube(3, 5, 4)
print(a)