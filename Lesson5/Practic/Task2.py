x = 6
numbers_list = [2, 3, 4, 5, 6, 7, 8, 9]
square_prime_numbers = []


def square():
    return x ** 2


for numbers in numbers_list:
    count = 0
    for i in range(1, numbers + 1):
        if (numbers % i == 0):
            count += 1
    if (count == 2):
        square_prime_numbers.append(numbers ** 2)


print(square())
print(square_prime_numbers)
