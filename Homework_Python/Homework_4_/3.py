# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# str = input('Задайте последовательность чисел, числа разделите через пробел: ')
# число можно повторить несколько раз:')
# list = str.split()
# list_1 = []
# count = 0
# for i in range(1, len(list)):
#     if (i == len(list) - 1):
#         if list[i-1] != list[i]:
#             list_1.append(list[i])
#         break
#     elif (list[i-1] != list[i]) and (int(list[i+1]) == int(list[i]) + 1):
#         list_1.append(list[i])

str = input('Задайте последовательность чисел, числа разделите через пробел: ').split()
# a = [1, 2, 2, 2 , 3, 1, 4]
# print(set(a))
b = list(filter(lambda x: str.count(x) == 1, str))
print(b)