class EvenRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0

    def __next__(self):
        if self.start <= self.end:
            if self.start % 2 == 0:
                print(f"{self.start}")
                self.start += 2
            else:
                self.start += 1
        else:
            raise StopIteration("Out of numbers!")

    def __iter__(self):
        return self


r = EvenRange(5, 15)

next(r)
next(r)
next(r)
next(r)
next(r)
next(r)
next(r)
