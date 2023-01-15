# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# from random import randint
# list_1 = []
# n = int(input('Введите длину списка: '))
# for i in range(n):
#     list_1.append(randint(1, 10))
# print(list_1)
# list_2 = []
# i = 0
# j = n - 1
# while (i <= j):
#     list_2.append(list_1[i] * list_1[j])
#     i += 1
#     j -= 1
# print(list_2)

import random
b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list(random.randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)
