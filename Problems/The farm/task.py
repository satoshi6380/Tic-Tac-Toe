CHICKEN, GOAT, PIG, COW, SHEEP = 23, 678, 1296, 3848, 6769
money = int(input())

if money < CHICKEN:
    print('None')
elif money // SHEEP > 0:
    print(money // SHEEP, 'sheep')
elif money // COW > 0:
    print(money // COW, 'cow' if money // COW == 1 else 'cows')
elif money // PIG > 0:
    print(money // PIG, 'pig' if money // PIG == 1 else 'pigs')
elif money // GOAT > 0:
    print(money // GOAT, 'goat' if money // GOAT == 1 else 'goats')
elif money // CHICKEN > 0:
    print(money // CHICKEN, 'chicken' if money // CHICKEN == 1 else 'chickens')