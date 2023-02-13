from pymonad.writer import Writer
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return Writer(x + y, f"Called function 'add' with arguments {x} and {y}. Result: {x + y}")

@curry(2)
def mul(x, y):
    return Writer(x * y, f"Called function 'mul' with arguments {x} and {y}. Result: {x * y}")

logged_arithmetic = (Writer
                     .insert(0)
                     .then(add(1))
                     .then(mul(2)))
print(logged_arithmetic)