# 3.Вводится список в виде вещественных чисел в одну строку через пробел.
# Сначала нужно сформировать список из введенной строки.
# Затем, все отрицательные значения в этом списке заменить на -1.0.
# Результат вывести на экран в виде строки чисел через пробел.
# Программу следует реализовать с использованием функции enumerate.

# str = input('Введите список вещественных чисел через пробел: ')
# list_1 = list(map(float, str.split()))
# print(list_1)
# for i in range(len(list_1)):
#     if list_1[i] < 0:
#         list_1[i] = -1.0
# list_2 = list(map(str, list_1))
# print(', '.join(list_2))
# answer = list(enumerate(list_2))
# print(answer)

a=list(map(float,input().split()))

for i ,r in enumerate(a):
    if r<0:
        a[i]=-1.0

# for i in range(len(a)):
#     if a[i] < 0:
#         a[i]= -1.0

print(*a)