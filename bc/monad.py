from bc.tools import checker
from pymonad.either import Left

def m_condition(*args):
    c = checker(*args)
    
    def inner(obj):
        result = c(obj)
        if len(result) > 0:
            return Left('; '.join(result))
        else:
            return obj
        
    return inner