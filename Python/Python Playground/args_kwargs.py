def add(*numbers):
    summation = 0
    print(type(numbers))
    for i in numbers:
        summation += i
    return summation


print(add(1, 2, 3, 4))
