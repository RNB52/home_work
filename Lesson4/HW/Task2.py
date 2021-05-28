import re
res = str()
my_file =  open(r'D:\Курсы\Урок3\Домашка\numbers.txt')
my_file1 =  open('numbers_result.txt', "w")

              
data = my_file.readline()
num_list = re.findall('\d+', data)

fizz = int(num_list[0])           
buzz = int(num_list[1])
third_number = int(num_list[2])
    
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
my_file1.write(res)
my_file.close()
my_file1.close()
