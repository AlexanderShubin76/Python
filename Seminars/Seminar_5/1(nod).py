# 1. Рассчитать нод двух чисел(быстрый и медленный способ)

# num_1 = int(input('Введите первое число:'))
# num_2 = int(input('Введите второе число:'))
# def fun(num):
#     list = []
#     a = 2
#     while num>=2:
#         if (not num%a):
#             list.append(a)
#             num = num/a
#         else:
#             a+=1
#     return list   

# list_1 = fun(num_1)     
# list_2 = fun(num_2)
# list_3 = []
# print(list_1)
# print(list_2)
# for x in list_1:
#     if x == list_2[0]:
#         list_3.append(x)
#         list_1 = list_1[1:]
#         list_2 = list_2[1:]
        
#     else:
#         list_1 = list_1[1:]
# # list_1 = list(filter(lambda x: ,[x for x in fun(num_1)]
# # print(list_1)

# print(list_3)
# import math
# print(math.prod(list_3))

# num_1 = int(input('Введите первое число:'))
# num_2 = int(input('Введите второе число:'))
# def fun(x, y):
#     min = x
#     if y > x:
#         min = y
#     number = None
#     for i in range(int(min/2)+1, 1, -1):
#         if (x%i == 0 and y%i ==0):
#             number = i
#             break
#     if number == None:
#         print('НОД не найден')
#     else:
#         print(f'НОД равен {number}')

# fun(num_1, num_2)

# num_1 = int(input('Введите первое число:'))
# num_2 = int(input('Введите второе число:'))

# def f(a, b):
#     while (a != b):
#         if a>b:
#             a = a-b
#         else:
#             b = b-a
#     return a

# print(f'НОД равен {f(num_1, num_2)}')

num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))

def f(a, b):
    
    if a < b:
        a, b = b, a
    while (b!= 0):
        a , b = b , a%b
    return a

print(f'НОД равен {f(num_1, num_2)}')