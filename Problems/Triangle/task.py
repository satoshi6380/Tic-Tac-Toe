num = int(input())
for x in range(num):
    y = x * 2 + 1
    print(('#' * y).center(num * 2 - 1))
