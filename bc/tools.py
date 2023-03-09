from collections import namedtuple

###############################################################################
# Curry functions
#
def curry1(fn):
    def first(arg):
        return fn(arg)
    return first

def curry2(fn):
    def inner1(second_argument):
        def inner2(first_argument):
            return fn(first_argument, second_argument)
        return inner2
    return inner1

def curry3(fn):
    def inner1(third_argument):
        def inner2(second_argument):
            def inner3(first_argument):
                return fn(first_argument, second_argument, third_argument)
            return inner3
        return inner2
    return inner1

def retarg(arg):
    """Returns argument passed in. Identity function for pass-through.

    Args:
        arg (): whatever argument is passed in.

    Returns:
        _type_: same as 'arg' parameter.
    """
    return arg


###############################################################################
# Miscellaneous functions
#
def copy_namedtuple_except(NT_CLASS, nt, key, value):
    """Creates copy of argument namedtuple 'nt', replacing one field value for argument 'value'

    Args:
        NT_CLASS (_type_): class name of namedtuple (i.e. Person)
        nt (_type_): namedtuple to copy.
        key (_type_): name of attribute to replace.
        value (_type_): value of attribute.

    Returns:
        _type_: If copy succeeds, returns copy of 'nt'; otherwise, returns 'nt' as pass-through
    """
    if nt != None and hasattr(nt, key):
        d = nt._asdict()
        d[key] = value
        return NT_CLASS(**d)

    return nt


###############################################################################
# Validator functions
#
def validator(msg, fn):
    """Encapsulates a condition and a predicate function.

    Args:
        msg (str): error message applying to case when argument fn returns false.
        fn (function): predicate function that represents the condition
    """
    def inner(*args):
        return fn(*args)
    
    f = inner
    f.msg = msg
    return f

def checker(*args):
    """Configures checker function with validators in *args

    Returns:
        obj (): configured checker function
    """

    validators = args

    def inner(obj):
        """checker function

        Args:
            obj (): object validation is performed against

        Returns:
            list(str): if any of the validators in *args fail, then function returns list of validation error messages; otherwise, returns []
        """
        errs = [v.msg for v in validators if not v(obj)]
        return errs
    return inner

_identity = curry1(retarg)

less_than = curry2(lambda lhs, rhs: lhs < rhs)
greater_than = curry2(lambda lhs, rhs: lhs > rhs)

less_than_or_equal_to = curry2(lambda lhs, rhs: lhs <= rhs)
greater_than_or_equal_to = curry2(lambda lhs, rhs: lhs >= rhs)