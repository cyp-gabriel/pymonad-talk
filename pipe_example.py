from pymonad.reader import Compose, Pipe, Reader

def inc(x): 
    return x + 1

pipe_with_flush = (Pipe(0)
                    .then(inc)
                    .then(inc)
                    .flush())

result = pipe_with_plus = +(Pipe(0)
                            .then(inc)
                            .then(inc))
print(result)