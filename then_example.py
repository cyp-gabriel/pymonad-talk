from pymonad.maybe import Just

################################
# .then example

valid_result = (Just(100)
                .then(lambda x: x + 30)
                .then(lambda x: x - 50))
print(valid_result)