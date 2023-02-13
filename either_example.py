from pymonad.either import Either
from pymonad.maybe import Just
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

@curry(2)
def mul(x, y):
    return x * y

@curry(2)
def div(x, y):
    return x / y

e = (Either.insert(1)
    .then(add(7))
    .then(div(0))  # Returns a Left with a ZeroDivisionError
    .then(mul(5))
    .either(lambda e: 0, lambda x: x) # ignore the error and return 0
    ) # 'e' takes the value 0
