l = [1, 2, 3, 4, 5]
count_for = 0
count_while = 0
for i in range(len(l)):
      count_for += l[i]
print(count_for)

j = 0
while j < len(l):
    count_while += l[j]
    j = j + 1
print(count_while)    
