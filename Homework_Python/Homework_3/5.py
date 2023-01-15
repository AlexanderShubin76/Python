# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# n = int(input('Задайте число:'))


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)



# def negafib(j):
#     if j == -1:
#         return 1
#     if j == -2:
#         return -1
#     else:
#         return negafib(j+2) - negafib(j+1)

# list_fib = []

# for e in range(n+1):
#     list_fib.append(fib(e))

# list_negafib = [None] * n

# for e in range (1, n+1):
#     list_negafib[-e] = negafib(-e)

# print(list_negafib + list_fib)

def lst_fibonacci_num():
    num = int(input('Введите любое натуральное число: '))
    fib = []
    a, b = 1, 1
    for i in range(num):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for j in range(num + 1):
        fib.insert(0, a)
        a, b = b, a - b
    print(f'Список чисел Фибоначчи для {num}: {fib}')


lst_fibonacci_num()