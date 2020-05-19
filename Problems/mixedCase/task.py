words = input().split(maxsplit=1)
if len(words) > 1:
    words[1] = words[1].title().replace(' ', '')
print(''.join(words))
