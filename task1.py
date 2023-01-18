def geometric_mean(a, b):
    try:
        return round((a * b)**0.5, 5)
    except Exception as err:
        return f"Error: {err}"


print(geometric_mean(3, -5))
print(geometric_mean(4, 5))
print(geometric_mean("3", 8.0))







