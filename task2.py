
def get_odd_num(num):
    while True:
        if (num % 2) != 0:
            yield num
        num += 1


l = get_odd_num(6)
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))









