import sys

arr = [10, 20, 50, 100, 200, 500, 1000]

user_money = int(input())
if not user_money or user_money % 10 or user_money > sum(map(lambda x: x * 10, arr)):
    sys.exit(0)

bancnots = dict.fromkeys(arr, 0)

for cur_amount in bancnots:
    for i in range(10, 0, -1):
        if not(user_money - i * cur_amount) or (user_money - i * cur_amount) > 0:
            bancnots[cur_amount] = i
            user_money -= i * cur_amount
            break
print(bancnots)