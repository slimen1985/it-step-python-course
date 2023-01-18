def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    print(x, a, y)


def bar(a):
    try:
        foo(a)
    except ZeroDivisionError as err:
        return f"Error: {err}"


def bzz(a):
    try:
        bar(a)
    except IndexError as ERR:
        return f"Error: {ERR}"


print(bzz(0))
print(bzz(4))
print(bzz(2))