
def validator(msg, fn):
    def inner(*args):
        return fn(*args)
    
    f = inner
    f.msg = msg
    return f

# validator encapsulates a predicate function and an associated error message
greater_than10 = validator("must be greater than 10", lambda x: x > 10)
print(f"valid result: {greater_than10(11)}")
print(f"invalid result: {greater_than10(5)}")

def checker(*args):
    validators = args

    def inner(obj):
        errs = [v.msg for v in validators if not v(obj)]
        return errs
    return inner

"""checker encapsulates a set of validators.  In effect they represent a
   condition.
"""

less_than20 = validator("must be less than 20", lambda x: x < 20)

within_range = checker(less_than20, greater_than10)

print(f"valid result: {within_range(11)}")
print(f"valid result: {within_range(-1)}")