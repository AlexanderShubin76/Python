# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
num = int(input('Введите число: '))
strk = ""
a = num
while (a != 0):
    strk = str(a % 2) + strk
    a = a//2
print(f'Число "{num}" в двоичной системе будет выглядеть как "{strk}"')
