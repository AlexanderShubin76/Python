# Доп 7. Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элементов списка,
# стоящих не нечетной позиции.
from random import randint

list = [randint(0, 100) for x in range(10)]
list_1 = []
for x,r in enumerate(list):
    if x%2 == 0:
        list_1.append(r)
print(list)
print(list_1)
result = sum(list_1)
print(result)
result_1 = sum(filter(lambda x: x%2, list))
print(result_1)