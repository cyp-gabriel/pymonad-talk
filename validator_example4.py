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


###############################################################################
# Validator example
#
def render_person(p):
    s = f"First name: {getattr(p, 'fname')}"
    s += f"\nLast name: {getattr(p, 'lname')}"
    s += f"\nAge: {getattr(p, 'age')}"
    s += f"\nSex: {getattr(p, 'sex')}"
    return s

fields = ('fname', 'lname', 'age', 'hotness', 'sex')
Person = namedtuple("Person", fields, defaults=(None,) * len(fields))
p = Person('bill', 'esquire', 25, 6, 'm')

# set up pre- and post-conditions
pre = condition(
    validator("Person age must be an adult", lambda p: greater_than(20)(p.age)),
    validator("Person must be male", lambda p: p.sex == 'm'))

post = condition(
    validator("age must be less than 45", lambda p: less_than(45)(p.age)),
    validator("age must be greater than 10", lambda p: greater_than(10)(p.age)))

# this is the processing step
increase_age = lambda p, new_age: copy_namedtuple_except(type(p), p, 'age', p.age + new_age)
inc_age = curry2(increase_age)

# set up chain
render = (Either.insert(p)
          .then(pre)
          .then(inc_age(10))
          .then(post)
          .then(render_person))
print(f"\nSUCCESS pipe\n\n{render}")


p2 = Person('bill', 'esquire', 0, 6, 'm')

render = (Either.insert(p2)
          .then(pre)
          .then(inc_age(10))
          .then(post)
          .then(render_person))
print(f"\nFAILURE pipe\n\n{render}\n")
