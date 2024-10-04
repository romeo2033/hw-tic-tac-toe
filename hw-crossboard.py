board = list(['-'] * 3 for i in range(3))  # генератор двумерного списка для создания игровой доски


def board_output():  # функция для вывода игрового поля
    print()
    print('   ', end='')  # вывод отступа в левом верхнем углу равен одному символу и табуляции
    for i in range(3):  # вывод нумерации столбцов
        print(f'{i}', end='  ')
    print()

    row_number = 0  # переменная для нумерации строк
    for row in board:
        print(row_number, end='  ')  # вывод номера строки с отступом в 1 табуляцию
        row_number += 1
        for field in row:
            print(field, end='  ')
        print()


def turn():  # функция для совершения игроком хода
    row, col = '', '' # объявление переменных дабы избежать возможность использования до их инициализации
    while True:  # цикл для проверки правильности ввода координат через try except и проверку условий
        try:
            turn_player = input('Введите координаты, куда хотите сходить в формате: ряд, столбец \nВвод: ')
            row, col = turn_player.replace(' ', '').split(',')
            row, col = int(row), int(col)
        except ValueError:  # проверка на ошибку ValueError
            print('\nВведен неверный формат: нужно ввести ЦИФРЫ от 0 до 2 через запятую без лишних символов!')
            continue
        if 0 <= row <= 2 and 0 <= col <= 2:  # проверка на то что координаты реальны
            if board[row][col] == '-':  # проверка занятости поля по данным координатам
                break
            else:
                print('\nЭто поле занято, выберите другие координаты!')
        else:
            print('\nВведен неверный формат: нужно ввести цифры от 0 до 2!')
    return row, col


def check_winner():  # функция для проверки, есть ли победитель
    # проверка строк
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return row[0]

    # проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    # проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

        # проверка на отсутствие ничьей
    for row in board:
        if "-" in row:
            return None  # игра продолжается

    # если все клетки заполнены и нет победителя, это ничья
    return "draw"


while True:  # игровой цикл | прерывается только в случае победы игрока
    board_output()

    print('\nИгрок 1')
    r, c = turn()
    board[r][c] = 'o'  # запись хода игрока

    if check_winner():  # проверка на победителя
        board_output()
        sign = check_winner()
        if sign == 'o':
            print('\nПобедитель игрок 1!\nПоздравляю!')
        elif sign == 'x':
            print('\nПобедитель игрок 2!\nПоздравляю!')
        else: print('\nБоевая ничья!\nПожмите руки.')
        break  # если есть победитель - цикл завершается / игра окончена

    board_output()

    print('\nИгрок 2')
    r, c = turn()
    board[r][c] = 'x'

    if check_winner():
        board_output()
        sign = check_winner()
        if sign == 'o':
            print('\nПобедитель игрок 1!\nПоздравляю!')
        elif sign == 'x':
            print('\nПобедитель игрок 2!\nПоздравляю!')
        else:
            print('\nБоевая ничья!\nПожмите руки.')
        break


