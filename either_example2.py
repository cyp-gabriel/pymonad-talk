from pymonad.either import Either, Left
from pymonad.maybe import Just
from pymonad.tools import curry
from functools import partial

def curry2(fn):
    def inner1(second_argument):
        def inner2(first_argument):
            return fn(first_argument, second_argument)
        return inner2
    return inner1

def _add(x, y):
    return x + y

def _mul(x, y):
    return x * y

def _div(x, y):
    if y == 0:
        return Left("Division by zero unacceptable, fiend.")
    else:
        return x / y

n = 1
#add = curry2(_add)(n)
add = curry2(_add)
#mul = curry2(_mul)(n)
mul = curry2(_mul)
#div = curry2(_div)(n)
div = curry2(_div)

e = (Either.insert(1)
    .then(add(7))
    .then(div(0))  # Returns a Left with a ZeroDivisionError
    .then(mul(5)))
print(e)


