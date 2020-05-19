names = []
count = 0
for _ in range(int(input())):
    x = input().split()
    if x[1] == 'win':
        names.append(x[0])
        count += 1

print(names)
print(count)
