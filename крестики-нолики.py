def greeting():
    print('-----------')
    print('Добро пожаловать в игру \n КРЕСТИКИ-НОЛИКИ')
    print('-----------')

def show():
    print('   0 1 2')
    print('  ______')
    for i in range(3):
        row = " ".join(field[i])
        print(f'{i}| {row}')


def request_a_move():
    while True:
        num_cell = input("Ведите 2 числа от 0 до 2. Ваш ход: ").split()

        if len(num_cell) != 2:
            print(" Введите 2 числа! ")
            continue

        x, y = num_cell

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" введите числа от 0 до 2 ")
            continue

        if field[x][y] != " ":
            print(" Ячейка занята! ")
            continue

        return x, y


def check_win():
    win_combo = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for combinatoin in win_combo:
        symbols = []
        for c in combinatoin:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greeting()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = request_a_move()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break

