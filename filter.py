# filter() = creates a collection of elements from an iterablr for which a function returns

# filter(function, iterable)

friends = [("Rachel", 20),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chadler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 17

human = list(filter(age , friends))

for i in human:
    print(i)