# 1. Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
from random import randint
n = int(input('Введите длину списка: '))
list = []
for i in range(n):
    list.append(randint(-100, 100))
print(''.join(str(list)))