text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

num = int(input())
li = []
for x in text:
    for y in x:
        if len(y) <= num:
            li.append(y)
print(li)
