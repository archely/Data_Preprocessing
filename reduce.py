import functools

factorial = [2,4,5,6]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)

