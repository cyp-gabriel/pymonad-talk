from pymonad.list import *
from pymonad.tools import curry

# Takes a simple number type and returns a 'List' containing that value and it's negative.
def positive_and_negative(x):
    return ListMonad(x, -x)

# You can call 'positive_and_negative' normally.
x = positive_and_negative(9)        # returns List(9, -9)
print(x)

# Or you can create a List...
x = ListMonad(9).then(positive_and_negative)        # also returns List(9, -9)
print(x)

# ... and then use '>>' to apply positive_and_negative'

# But 'x' could also have more than one value...
x = ListMonad(1, 2).then(positive_and_negative)        # returns List(1, -1, 2, -2)
print(x)

# And of course you can sequence partially applied functions.
@curry(2)
def add_and_sub(x, y):
    return ListMonad(y + x, y - x)

#ListMonad(2) >> positive_and_negative >> add_and_sub(3)
l = (ListMonad(2)
     .then(add_and_sub(3))
     .then(positive_and_negative))
print(l)