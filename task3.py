def get_pairs(lst: list) -> list[tuple]:

    d = {}
    count = 0
    if len(lst) == 1:
        return None
    else:
        for i in lst:
            if len(lst) - 1 > count:
                d[i] = lst[count + 1]
                count += 1
            else:
                return list(d.items())


pairs = input('Enter list: ')
print(get_pairs(pairs))

















