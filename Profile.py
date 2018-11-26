from timeit import default_timer as timer
from types import FunctionType

def profile(func):
    def wrapper():
        if isinstance(func, FunctionType):
            perform(func)
        else:
            for idx in func.__dict__:
                if isinstance(func.__dict__[idx], FunctionType):
                    perform(func.__dict__[idx], True)
    return wrapper()

def perform(func, isClass = False):
    print(func.__qualname__, "Начало работы")
    startTim = timer()
    if isClass:
        func
    else:
        func()
    endTime = timer() - startTim
    print('{} закончила работу за {} секунд'.format(func.__qualname__, endTime))


@profile
def func():
    x = 3
    x = x + 3

@profile
class Bar:
    def __init__(self):
        pass
    def func(self):
        x = 3
        x = x - 5
        y = x

func()
Bar()