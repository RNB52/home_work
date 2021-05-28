my_file = open(r'D:\Курсы\Урок3\Домашка\numbers.txt')

for j in range(1, 21):
    data = my_file.readline()
    data = data.split()

    fizz = int(data[0])
    buzz = int(data[1])
    third_number = int(data[2])

    print()
    for i in range(1, third_number + 1):
        if not(i % fizz) and not(i % buzz):
            print('FB', end=" ")
        elif not(i % fizz):
            print('F', end=" ")
        elif not(i % buzz):
            print('B', end=" ")
        else:
            print(i, end=" ")
my_file.close()
