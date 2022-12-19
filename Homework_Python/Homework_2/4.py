# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке ( пример n=4, lst1=[4,-2,1,3]
# - список на основе n, а позиции элементов lst2=[3,1].
from random import randint
list_1 = []
list_2 = []
n = int(input('Введите значение N > 0: '))
if (n > 0):
    for i in range(n):
        list_1.append(randint(-n, n))
    print('list_1 =', ''.join(str(list_1)))
    for i in range(randint(1, n)):
        list_2.append(randint(0, n-1))
    print('list_2 =', ''.join(str(list_2)))
    result = 1
    for i in list_2:
        result *= list_1[i]
    print(
        f'Произведение элементов списка list_1 на позициях списка list_ 2 равно: {result}')
else:
    print('Ошибка ввода')
