# 2 b. Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
a = int(input('Введите общее количество конфет для игры: '))
gamer_1 = input('Введите имя игрока: ')
gamer_1_num = randint(1,2)
if gamer_1_num == 1:
    print('Случайным образом выбрано, что первым ходите Вы. Бот ходит вторым')
    while(a!=0):
        print(f'Общее количество конфет: {a}')
        a_1 = int(input(f'{gamer_1}, выберете количество конфет (не более 28): '))
        while (a_1 > 28 or a_1 < 0):
            a_1 = int(input(f'{gamer_1}, Вы выбрали более 28 конфет, выберете количество конфет (не более 28): '))
        a -=a_1
        if (not a):
            print(f'Поздравляем!!! {gamer_1}, Вы - победитель!')
            break
        elif (a < 0):
            print('Вы плохо считаете. Ход достается боту')
            a+=a_1
            
        print(f'Общее количество конфет: {a}')
        
        if a <= 28:
            a_2 = a
        else:
            if 30 <= a <= 57:
                a_2 = a - 29
          
            else:
                a_2 = a%28 - 2
                if -2<a_2 <= 0:
                    a_2 = 1
                elif a%28 == 0:
                    a_2 = 26
        a -=a_2
        
        print (f'Бот выбрал {a_2} конфет')
        
        if (not a):
            print('К сожалению, Вы проиграли! Бот выиграл.')
            break
        
else:
    print('Случайным образом выбрано, что первым ходит бот. Вы ходите вторым.')
    while(a!=0):
        print(f'Общее количество конфет: {a}')
        if a <= 28:
            a_1 = a
        else:
            if 30 <= a <= 57:
                a_1 = a - 29
            else:
                a_1 = a%28 - 2
                if -2<a_1 <= 0:
                    a_1 = 1
                elif a%28 == 0:
                    a_1 = 26
        a -=a_1
   
        print (f'Бот выбрал {a_1} конфет')
        if (not a):
            print('К сожалению, Вы проиграли! Бот выиграл.')
            break

        print(f'Общее количество конфет: {a}')
        
        a_2 = int(input(f'{gamer_1}, выберете количество конфет (не более 28): '))
        while (a_2 > 28 or a_2 < 0):
            a_2 = int(input(f'{gamer_1}, Вы выбрали более 28 конфет, выберете количество конфет (не более 28): '))
        a -=a_2
        if (not a):
            print(f'Поздравляем!!! {gamer_1}, Вы - победитель')
            break
        elif (a < 0):
            print('Вы плохо считаете. Ход достается боту')
            a+=a_2

