from bc.tools import checker
from pymonad.either import Left
from pymonad.maybe import Just, Nothing
from pymonad.either import Either


def process_value(value):
    """Does simple transform on value argument. (adds 30 to value)
    
    Pre-condition(s):
    - value argument must be positive

    Post-condition(s):
    - value must be between 50 and 100

    Args:
        value (int): integer value; must pass pre-conditions
    Returns:
        Just monad wrapped integer value between 50 and 100 if valid, or Nothing if processed value fails pre- or post-conditions.
    """

    # pre-condition check
    if value < 0:
        return Nothing

    # processing/transforming input value
    new_value = value + 30

    # post-condition check
    if not (new_value >= 50 and new_value <= 100):
        return Nothing
    
    return Just(new_value)

def validator(msg, fn):
    def inner(*args):
        return fn(*args)
    
    f = inner
    f.msg = msg
    return f

def checker(*args):
    validators = args

    def inner(obj):
        errs = [v.msg for v in validators if not v(obj)]
        return errs
    return inner

"""we need to create a checker that returns a Left if any validators
   fail.
"""
def m_condition(*args):
    c = checker(*args)
    
    def inner(obj):
        result = c(obj)
        if len(result) > 0:
            return Left('; '.join(result))
        else:
            return obj
        
    return inner



"""Instead of doing this, we can seperate out the pre- and post-conditions
   using checker and validator.  One checker could handle the pre-conditions,
   and another checker could encapsulate the post-conditions.
"""

within_range = m_condition(
    validator("must be greater than 0", lambda x: x > 0),
    validator("must be less than 50", lambda x: x < 50))

valid_result = (Either.insert(25)
                .then(within_range))
print(valid_result)

invalid_result = (Either.insert(100)
                  .then(within_range))
print(invalid_result)