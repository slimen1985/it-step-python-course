def fib():
    fib1 = fib2 = 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))