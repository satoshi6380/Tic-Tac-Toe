dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
is_ok = True
for word in words:
    if word not in dictionary:
        print(word)
        is_ok = False
if is_ok:
    print('OK')
