# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
list_1 = []
n = int(input('Введите длину списка: '))
for i in range(n):
    list_1.append(randint(1, 10))
print(list_1)
list_2 = []
i = 0
j = n - 1
while (i <= j):
    list_2.append(list_1[i] * list_1[j])
    i += 1
    j -= 1
print(list_2)
