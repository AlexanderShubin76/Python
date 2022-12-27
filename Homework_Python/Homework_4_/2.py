# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N , больше 1: '))

if n < 2:
    print('Ошибка ввода')

else:
    list = []
    list_1 = []

    for i in range(2, n+1):
        list.append(i)

    for j in list:
        for k in list:
            if k % j == 0 and k != j:
                list.remove(k)

    for s in list:
        if n % s == 0:
            list_1.append(s)

    print(f'Список простых множителей числа "{n}": {list_1}')
