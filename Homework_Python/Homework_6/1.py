# 1. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

str = input('Задайте последовательность чисел через пробел: ').split()
b = list(filter(lambda x: str.count(x) == 1, str))
print(b)