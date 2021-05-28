res = str()
my_file = open(r'D:\Курсы\Урок3\Домашка\numbers.txt')
my_file1 = open('numbers_result.txt', "w")

for j in range(1, 21):
    data = my_file.readline()
    data = data.split()

    fizz = int(data[0])
    buzz = int(data[1])
    third_number = int(data[2])

    print()
    res = ('')
    for i in range(1, third_number + 1):
        if not(i % fizz) and not(i % buzz):
            res += 'FB'
            print('FB', end=" ")
        elif not(i % fizz):
            res += 'F'
            print('F', end=" ")
        elif not(i % buzz):
            res += 'B'
            print('B', end=" ")
        else:
            res += str(i)
            print(i, end=" ")
        res += ' '
    res += '\n'
        
    my_file1.write(res)
my_file.close()
my_file1.close()
