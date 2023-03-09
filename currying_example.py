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
   With currying you can create expressive APIs
"""

less_than = curry2(lambda lhs, rhs: lhs < rhs)
greater_than = curry2(lambda lhs, rhs: lhs > rhs)

"""
   Currying allows you to configure a muli-argument function with n numbe
   of arguments.  When using a pipe or compose, one variable is passed 
   down the chain, currying is useful.
"""

"""Partial 

   Currying functions evaluate arguments from right to left, whereas
   partial evaluates arguments from left to right.
"""

def rgb(r, g, b):
    return f"#{hex(r)}{hex(g)}{hex(b)}".replace("0x", "").upper()

red_color = partial(rgb, 255)
print(f"red_color(50, 50) = {red_color(50, 50)}")

red_green_color = partial(rgb, 255, 255)
print(f"red_green_color(37) = {red_green_color(37)}")


"""
   Both functions allow you to configure a function with arguments.

   When setting up a pipeline, we need to create functions that accept
   one argument: the argument being passed through the pipeline.
"""

greater_than10 = greater_than(10)

x = 5
if greater_than10(x):
    print("x is greater than 10")
else:
    print("x is not greater than 10")