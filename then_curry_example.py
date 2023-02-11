from pymonad.maybe import Just, Nothing
from pymonad.tools import curry

################################
# .then example

# value: 50 > value > 100
@curry(2)
def increase_value(inc, value):
    new_value = value + 30
    return Just(new_value) if new_value >= 50 and new_value <= 100 else Nothing
    
# value: 50 > value > 100
@curry(2)
def decrease_value(dec, value):
    new_value = value - 50
    return Just(new_value) if new_value >= 50 and new_value <= 100 else Nothing
    
inc_30 = increase_value(30)
dec_50 = decrease_value(50)

res = Just(70) \
    .then(inc_30) \
    .then(dec_50)

print(res)