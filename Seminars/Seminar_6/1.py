# 1. Вводится список целых чисел в одну строчку через пробел.
# Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter.
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23
list_numbers_0 = map(int, input('Введите список целых чисел в одну строчку через пробел: ').split())
list_numbers = list(filter(lambda x: len(str(abs(x))) == 2, list_numbers_0))
            
print(* list_numbers)