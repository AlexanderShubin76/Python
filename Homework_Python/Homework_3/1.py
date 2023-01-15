
# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
list = []
for i in range(10):
    list.append(randint(-10, 10))
print(list)
# result = 0
# for k in range(1, len(list)):
#     if (k % 2 != 0):
#         result += list[k]

print(sum(list[1::2]))
# print(f'Сумма элементов на нечетных позициях: {result}')
