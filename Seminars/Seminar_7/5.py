# 5. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
lst = list(filter(lambda x: not x ** 0.5%9, map(lambda x: x**2, [x for x in range(10,100)])))
# summa = sum(filter(lambda x: not x ** 0.5%9, map(lambda x: x**2, [x for x in range(10,100)])))
summa = sum(map(lambda x: x**2, filter(lambda x: x%9 ==0, [x for x in range(10, 100)])))
print(*lst)
print(summa)
