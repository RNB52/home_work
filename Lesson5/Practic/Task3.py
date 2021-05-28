from collections import Counter

my_file = open(r'D:\Курсы\Урок5\Практика\text.txt')
data = my_file.readline()
data = data.split()

count = Counter(list(map(lambda x: x.lower(), data)))
print(count)

my_file.close()
