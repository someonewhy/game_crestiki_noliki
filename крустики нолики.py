""" После Вебинара ,я изменил строку в функции приветствия "hi ()", сделал всё одной строкой
 и в конце кода сделал условия длся старта игры, добавил функцию "cont ()",которая спрашивает
у игрока хочет он продолжить или нет,создал две переменные"counter_o " и "counter_x",которые считают победы Х или 0
"""
def hi():
    print("\n Игра кретиски нолики\n",'Приветсвует вас\n', 'Используем две координаты:X и Y\n')

def show_feild():
    print('  |0 | 1| 2|','  __________',sep='\n')

    for i,row in enumerate(field):
        row_str= str(i) + ' |' + ' |'.join(map(str,row)) + ' |'
        print(row_str)
        print("  __________")
def ask():
    while True:
        cords =input("Ваш ход:").split()
        if len(cords) != 2:
            print(f'введите две координаты')
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print("введите числа")
        x,y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(f'Координаты вне диапозона')
            continue
        if field[x][y] !=" ":
            print('Клетка занята')
            continue
        return x, y
def check_win():
    global counter_x,counter_o

    win_cords= (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            counter_x += 1
            print(f"Выиграл X!!!\nСо счётом X-{counter_x}: O-{counter_o}")
            cont()
            return True
        if symbols == ["0", "0", "0"]:
            counter_o += 1
            print(f"Выиграл 0!!!\nСо счётом O-{counter_o}: X-{counter_x}")
            cont()
            return  True
    return False
def cont():
    global field
    qutstion = input('Хотите продолжить введите "да" или выйти введите "закончить": ')
    if 'да' in qutstion:
        field = [[" "] * 3 for i in range(3)]
        return run()
    elif 'закончить' in qutstion:
       return False
counter_x = 0
counter_o = 0
field= [[" "]*3 for i in range(3)]
def run():
    count = 0
    while True:
        count += 1
        if count % 2 == 1:
            print(" Ходит крестик!")
            show_feild()
        else:
            print(" Ходит нолик!")
            show_feild()

        x, y = ask()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if check_win():
            break

        if count == 9:
            print(" Ничья!")
            cont()
hi()
start = input('Для старта впишите"Вперёд": ')
if "Вперёд" in start:
    run()
else:
    print("Я вас не понял")