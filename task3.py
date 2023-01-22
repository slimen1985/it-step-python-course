def show_letters(some_str: str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])


any_str = show_letters("Bdsf23!121/fdfd")
print(next(any_str))
print(next(any_str))
print(next(any_str))
print(next(any_str))
print(next(any_str))
print(next(any_str))
print(next(any_str))


























