from bc.tools import validator, curry2, copy_namedtuple_except, less_than, greater_than
from collections import namedtuple
from pymonad.either import Either, Left

# encapsulates predicate and error message
def validator(msg, fn):
    def inner(*args):
        return fn(*args)
    
    f = inner
    f.msg = msg
    return f

v = validator('value must be greater than 0', lambda value: value > 0)
print(f"\n\nv(-1) = {v(-1)}")
print(f"v(20) = {v(20)}\n")

# encapsulates any number of validators
# runs all validators and returns array:
#   if there are errors
#      returns array with error messages
#   if not
#      returns empty array
def checker(*args):
    validators = args

    def inner(obj):
        errs = [v.msg for v in validators if not v(obj)]
        return errs
    return inner

c = checker(validator('value must be greater than 0', lambda value: value > 0),
            validator('value must be less than 50', lambda value: value < 50))
print(f"c(100) = {c(100)}")
print(f"c(15) = {c(15)}\n")

# Same as checker, except returns Left object containing
# error messages delimited by semicolon.  Otherwise, 
# returns object.
def condition(*args):
    c = checker(*args)
    
    def inner(obj):
        result = c(obj)
        if len(result) > 0:
            return Left('; '.join(result))
        else:
            return obj
        
    return inner

