# 3. Создайте программу для игры в ""Крестики-нолики"".
# Я написал программу, рассчитанную на игру человека с человеком!
print('Давайте приступим к игре Крестики-Нолики!')
from random import randint
massive = ['* * *'.split() for x in range(3)]
def print_array(mas):
    for i in range(len(mas)):
        for x in range(len(mas[i])):
            print(*mas[i][x], end ='  ')
        print()
print(f'Первоначальное поле для игры выглядит следующим образом:')
print_array(massive)
gamer_1 = input('Введите имя игрока №1: ')
gamer_2 = input('Введите имя игрока №2: ')
gamer_1_num = randint(1,2)
if gamer_1_num == 1:
    print(f'Случайным образом выбрано, что первым ходит {gamer_1}. Он будет "игрок №1", {gamer_2} - "игрок №2"')
else:
    print(f'Случайным образом выбрано, что первым ходит {gamer_2}. Он будет "игрок №1", {gamer_1} - "игрок №2"')
print('Игрок №1 ходит крестиками, игрок №2 ходит ноликами.')
count = 0
def game(name):
    print(f'{name} ваш ход!')
    x = int(input(f'{name}, введите положение по горизонтали(1-3). Ячейка должна быть пустой: ')) -1
    y = int(input(f'{name}, введите положение по вертикали(1-3). Ячейка должна быть пустой: '))-1
    while massive[x][y] == '0' or massive[x][y] == 'X':
            x = int(input(f'Ошибка ввода, ячейка заполнена. {name}, введите положение по горизонтали(1-3).'
                          f' Ошибка ввода, ячейка заполнена. Ячейка должна быть пустой на момент хода: ')) -1
            y = int(input(f'{name}, введите положение по вертикали(1-3). Ячейка должна быть пустой на момент хода: ')) -1

    if name == 'Игрок №1':
        massive[x][y] = 'X'
        print_array(massive)
        return 1
    else:
        massive[x][y] = '0'
        print_array(massive)
        return 1
def checking_win(massive, name):
    if ((massive[0][0] == '0' and massive[0][1] == '0' and massive[0][2] == '0') or
        (massive[1][0] == '0' and massive[1][1] == '0' and massive[1][2] == '0') or
        (massive[2][0] == '0' and massive[2][1] == '0' and massive[2][2] == '0') or
        (massive[0][0] == '0' and massive[1][0] == '0' and massive[2][0] == '0') or
        (massive[0][1] == '0' and massive[1][1] == '0' and massive[2][1] == '0') or
        (massive[0][2] == '0' and massive[1][2] == '0' and massive[2][2] == '0') or
        (massive[0][0] == '0' and massive[1][1] == '0' and massive[2][2] == '0') or
        (massive[0][0] == 'X' and massive[0][1] == 'X' and massive[0][2] == 'X') or
        (massive[1][0] == 'X' and massive[1][1] == 'X' and massive[1][2] == 'X') or
        (massive[2][0] == 'X' and massive[2][1] == 'X' and massive[2][2] == 'X') or
        (massive[0][0] == 'X' and massive[1][0] == 'X' and massive[2][0] == 'X') or
        (massive[0][1] == 'X' and massive[1][1] == 'X' and massive[2][1] == 'X') or
        (massive[0][2] == 'X' and massive[1][2] == 'X' and massive[2][2] == 'X') or
        (massive[0][0] == 'X' and massive[1][1] == 'X' and massive[2][2] == 'X')):
        print(f'{name}, поздравляем Вы выиграли!!!')
        return 100
    else:
        return 0
while count < 9:
    z = game('Игрок №1')
    s = checking_win(massive, 'Игрок №1')
    count+=z+s
    if count >9:
        break
    if count == 9:
        print('Ничья! Победила дружба!!!')
        break
    k = game('Игрок №2')
    a = checking_win(massive, 'Игрок №2')
    count+=k+a
