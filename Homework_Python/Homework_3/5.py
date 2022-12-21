# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('Задайте число:'))


def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

j = -n

def negafib(j):
    if j == -1:
        return 1
    if j == -2:
        return -1
    else:
        return negafib(j+2) - negafib(j+1)

list_fib = []

for e in range(n+1):
    list_fib.append(fib(e))

list_negafib = [None] * n

for e in range (1, n+1):
    list_negafib[-e] = negafib(-e)

print(list_negafib + list_fib)