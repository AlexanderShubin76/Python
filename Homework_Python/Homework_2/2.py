# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
list = []
n = int(input('Введите значение N >= 1: '))
if (n >= 1):
    for i in range(1, n+1):
        if (i == 1):
            list.append(i)
            continue
        list.append(i*list[len(list)-1])
    print(''.join(str(list)))
else:
    print('Некорректно введено значение N')
