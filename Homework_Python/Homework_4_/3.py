# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
str = input('Задайте последовательность чисел, числа разделите через пробел, одно и тоже \
число можно повторить несколько раз:')
list = str.split()
list_1 = []
count = 0
for i in range(1, len(list)):
    if (i == len(list) - 1):
        if list[i-1] != list[i]:
            list_1.append(list[i])
        break
    elif (list[i-1] != list[i]) and (int(list[i+1]) == int(list[i]) + 1):
        list_1.append(list[i])

print(f'Последовательность с неповторяющимися элементами: {list_1}')
