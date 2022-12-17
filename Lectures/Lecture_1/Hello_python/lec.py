# value = None
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 1234
# # print(type(value))
# s = "hello, world"
# # print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'. format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'. format(a, b, s))
# f = False
# # print(f)
# list = ['1', '2', '3']
# col = ['hello', 1, 2, 3, 4.5, True]
# print(list)
# print(col)

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, ' + ',  b, ' = ', a + b)
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')

# a = 1.312355555
# b = 3
# c = round(a*b, 7)
# print(c)
# a = 3
# a += 5
# print(a)

# f = 1 > 2 or 4 < 6

# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2
# print(is_odd)1

# if, else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар-топ)')
# else:
#     print('Привет, ', username)

# # while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# for
# r = range(10)
# for i in r:
#     print(i)

# for i in range(1,10 ,2):
#     print(i)

# for i in 'qwe rty':
#     print(i)

# Строки
text = 'съешь еще этих мягких французских булок'

# print(text[:])
# print(text[:2])



# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))

# for c in text:
#     print(c)

# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(len(numbers))
# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('gray')
# colors.remove('red')

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))