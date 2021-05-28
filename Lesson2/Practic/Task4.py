a = int(input())
l = list(str(a))

raz = 0
while a > 0:
    a = a // 10
    raz += 1
print('Количество разрядов:', raz)

m = 1
for i in l[::1]:
    i = int(i)
    print(i, "x", 10**(raz - m))
    m += 1