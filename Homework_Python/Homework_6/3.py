# 1. Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
from random import randint
list = [randint(-100, 100) for x in range(int(input('Введите количество элементов списка: ')))]
print(*list)