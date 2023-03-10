from pymonad.maybe import Just, Nothing

def increase_value(value):
    new_value = value + 30
    return new_value if not(new_value >= 50 and new_value <= 100) else Nothing
    
def decrease_value(value):
    new_value = value - 50
    return new_value if new_value >= 50 and new_value <= 100 else Nothing
    
valid_result = (Just(100)
                .then(increase_value)
                .then(decrease_value))

print(valid_result)


