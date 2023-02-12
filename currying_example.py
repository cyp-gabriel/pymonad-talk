from functools import partial

"""Currying explanation

   A curried function accepts a function as an argument which receives
   multiple arguments and returns a function that accepts one argument.
"""

def curry2(fn):
    def inner1(second_argument):
        def inner2(first_argument):
            return fn(first_argument, second_argument)
        return inner2
    return inner1

def add(x, y):
    return x + y

addN_to5  = curry2(add)(5)
n = 10
print(f"\nadd5_to({n}) = {addN_to5(n)}\n")

"""
   Currying allows you to configure a muli-argument function with n numbe
   of arguments.  When using a pipe or compose, one variable is passed 
   down the chain, currying is useful.
"""

"""Partial 

   Currying functions by evaluating arguments from right to left, whereas
   partial evaluates arguments from left to right.  Partial is useful for
   creating expressive APIs and handling *args and *vargs.
"""

def rgb(r, g, b):
    return f"#{hex(r)}{hex(g)}{hex(b)}".replace("0x", "").upper()

red_color = partial(rgb, 255)
print(f"red_color(50, 50) = {red_color(50, 50)}")

red_green_color = partial(rgb, 255, 255)
print(f"red_green_color(37) = {red_green_color(37)}")