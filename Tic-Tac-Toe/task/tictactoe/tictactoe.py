win_x = False
win_o = False
cells = list('         ')
player = 0


def print_cells():
    print('---------')
    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
    print('---------')


def enter_coordinates():
    global player

    xys = input('Enter coordinates:').split()
    # 数字かどうか　範囲内かどうか
    for xy in xys:
        if not xy.isdecimal():
            print('You should enter numbers')
            enter_coordinates()
        elif int(xy) < 1 or int(xy) > 3:
            print('Coordinates should be from 1 to 3!')
            enter_coordinates()
    # 埋まっているかどうか
    xy_num = (int(xys[0]) + 8) - 3 * int(xys[1])
    if cells[xy_num] == ' ':
        cells[xy_num] = 'X' if player % 2 == 0 else 'O'
        player += 1

        # ななめ
        check_result(cells[0] + cells[4] + cells[8])
        check_result(cells[2] + cells[4] + cells[6])

        # 横
        for i in range(3):
            word = ''
            for j in range(3):
                word += cells[i * 3 + j]
                check_result(word)

        # 縦
        for i in range(3):
            word = ''
            for j in range(3):
                word += cells[j * 3 + i]
                check_result(word)

        print_cells()

        if ' ' not in cells:
            print('Draw')
            exit()

        enter_coordinates()
    else:
        print('This cell is occupied! Choose another one!')
        enter_coordinates()


def check_result(word):
    if word in ['XXX', 'OOO']:
        print_cells()
        print(word[0], 'wins')
        exit()


# write your code here
print_cells()
enter_coordinates()
