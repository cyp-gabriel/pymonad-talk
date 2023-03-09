from pymonad.maybe import Just, Nothing

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

valid_value = process_value(20)
print(f"valid_value: {valid_value}")

invalid_value = process_value(-20)
print(f"invalid_value: {invalid_value}")

