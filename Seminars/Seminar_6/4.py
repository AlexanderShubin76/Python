# 4. Вводится натуральное число N.
# С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы.
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого
# угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано в примере ниже.

# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
number = int(input('Введите число: '))

list = [['1' if x == y else '0' for x in range(number)] for y in range(number)]
print(list)
for j in range(len(list)):
    for k in range(len(list[j])):
        print(*list[j][k], end = ' ')
    print()
