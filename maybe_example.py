from pymonad.maybe import Maybe, Nothing
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

@curry(2)
def sub(x, y):
    return x - y

@curry(2)
def mul(x, y):
    return x * y

@curry(2)
def div(x, y):
    if x == 0:
        return Nothing
    else:
        return y / x

e = (Maybe.insert(1)
     .then(add(7))
     .then(div(0))
     .then(mul(5)))






print(f"Failure: e = {e}")
