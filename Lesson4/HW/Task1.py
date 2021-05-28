import re                   
my_file =  open(r'D:\Курсы\Урок3\Домашка\numbers.txt')

              
data = my_file.readline()     
num_list = re.findall('\d+', data)      
   
fizz = int(num_list[0])           
buzz = int(num_list[1])
third_number = int(num_list[2])
    
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
