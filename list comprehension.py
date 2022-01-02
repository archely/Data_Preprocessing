# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

squares = []  # Create an empty list
for i in range(1, 11):  # Create a for loop
    squares.append(i * i)  # define what each loop iteration should do
print(squares)


students = [100, 90, 80, 70, 60, 30, 0]

#passed_students = list(filter(lambda x: x >= 60,  students))

#passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)