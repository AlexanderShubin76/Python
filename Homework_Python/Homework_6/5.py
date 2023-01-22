# 5. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке ( пример n=4, lst1=[4,-2,1,3]
# - список на основе n, а позиции элементов lst2=[3,1].
from random import randint
num = int(input('Задайте длину списка из N элементов, заполненных числами из промежутка [-N, N]: '))
list_1 = list(set([randint(-num, num) for x in range(num)]))
print(f'Список №1 чисел будет выглядеть следующим образом: {list_1}')
list_2 = list(set([randint(0, len(list_1)-1) for y in range(num)]))
print(f'Список №2 чисел с позициями будет выглядеть следующим образом: {list_2}')

result = 1
for i in range(len(list_2)):
    result *= list_1[list_2[i]]
print(f'Произведение элементов списка №1 с позициями, указанными в списке №2, будет равно: {result} ')