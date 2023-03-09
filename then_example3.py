from pymonad.maybe import Just, Nothing
from pymonad.tools import curry

@curry(2)
def increase_value(inc, value):
    new_value = value + 30
    return Just(new_value) if new_value >= 50 and new_value <= 100 else Nothing
    
@curry(2)
def decrease_value(dec, value):
    new_value = value - 50
    return Just(new_value) if new_value >= 50 and new_value <= 100 else Nothing
    
res = (Just(70)
       .then(increase_value(30))
       .then(decrease_value(50)))
print(res)


