# 1. Написать приложение сложения 2 чисел
sum = lambda x,y: x+y
x = int(input('Введите число x: '))
while not x.isdigit():
    print('Введите численное значение для x')
    x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
while not x.isdigit():
    print('Введите численное значение для y: ')
    y = int(input('Введите число y: '))
print(f'{x} + {y} = {sum}')