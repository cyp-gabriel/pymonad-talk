from bc.monad import mchecker
from bc.tools import validator, curry2, copy_namedtuple_except, less_than, greater_than
from collections import namedtuple
from pymonad.either import Either, Left

def to_s(p):
    s = f"First name: {getattr(p, 'fname')}"
    s += f"\nLast name: {getattr(p, 'lname')}"
    s += f"\nAge: {getattr(p, 'age')}"
    s += f"\nSex: {getattr(p, 'sex')}"
    return s

fields = ('fname', 'lname', 'age', 'hotness', 'sex')
Person = namedtuple("Person", fields, defaults=(None,) * len(fields))
p = Person('bill', 'esquire', 21, 6, 'm')

# set up pre- and post-conditions
pre = mchecker(
    validator("Person age must be an adult", lambda p: greater_than(20)(p.age)),
    validator("Person must be male", lambda p: p.sex == 'm'))

post = mchecker(
    validator("age must be less than 45", lambda p: less_than(45)(p.age)),
    validator("age must be greater than 10", lambda p: greater_than(10)(p.age)))

# this is the processing step
increase_age = lambda p, new_age: copy_namedtuple_except(type(p), p, 'age', getattr(p, 'age') + new_age)
inc_age = curry2(increase_age)

# set up chain
e = (Either.insert(p)
        .then(pre)
        .then(inc_age(10))
        .then(post)
        .then(to_s))
print(e)
