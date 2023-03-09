from pymonad.maybe import Just, Nothing, Maybe

def curry2(fn):
    def inner1(second_argument):
        def inner2(first_argument):
            return fn(first_argument, second_argument)
        return inner2
    return inner1

def div(n, d):
    if d == 0:
        return Nothing
    else:
        return n / d


div_by5 = curry2(div)(5)
result = Maybe.insert(10).then(div_by5)
print(f"result = Maybe.insert(10).then(div_by5) = {result}")

div_by0 = curry2(div)(0)
result = Maybe.insert(10).then(div_by0)
print(f"result = Maybe.insert(10).then(div_by0) = {result}")

