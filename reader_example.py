from pymonad.reader import Compose, Pipe, Reader

def inc(x): return x + 1
def dec(x): return x - 1

convoluted_inc_twice = (Compose(inc)
                        .then(inc)
                        .then(inc)
                        .then(dec))

c = convoluted_inc_twice(0) # Result: 2
print(c)