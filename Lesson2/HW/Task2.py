m = int(input())
n = int(input())
for i in range(m, n + 1):
    if not(i % 17):                   # число кратно 17
        print(i)
    elif i % 10 == 9:                 # число оканчивается на 9
        print(i)
    elif not(i % 3) and not(i % 5):  # число кратно 3 и 5 одновременно
        print(i)
