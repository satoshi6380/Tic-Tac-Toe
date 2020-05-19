# put your python code here
li, x = input().split(), input()
count = 0
vals = []
for num in li:
    if num == x:
        vals.append(str(count))
    count += 1

print(' '.join(vals) if len(vals) > 0 else 'not found')
