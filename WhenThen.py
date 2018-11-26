class ClassWhenThen:
    def __init__(self, func):
        self.listWhenAndThen = []
        self.pos = None
        self.func = func

    def when(self, func):
        def wrapper():
            if self.listWhenAndThen[self.pos]['then'] is None and not len(self.listWhenAndThen) is None:
                self.listWhenAndThen.append({'when': func, 'then': None})
                if self.pos is None:
                    self.pos = 0
                else:
                    self.pos = self.pos + 1
        return wrapper

    def then(self, func):
        def wrapper():
            if self.listWhenAndThen[self.pos]['then'] is None or len(self.listWhenAndThen):
                self.listWhenAndThen[self.pos]['then'] = func
        return wrapper

def whenthen(func):
    return ClassWhenThen(func)

@whenthen
def fract(x):
    return x * fract(x - 1)

@fract.when
def fract(x):
    return x == 0

@fract.then
def fract(x):
    return 1

@fract.when
def fract(x):
    return x > 5

@fract.then
def fract(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * fract(x - 5)