# 4.Саша и Галя коллекционируют монетки.
# Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через пробел.
# Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные.
# Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
Sasha_list = list(map(int, input('Введите список номиналов монеток Саши через пробел,'
             'значения дожны быть целочисленные:').split()))
print(f'Список Саши {Sasha_list}')
Galya_list = list(map(int, input('Введите список номиналов монеток Гали через пробел,'
             'значения дожны быть целочисленные:').split()))
print(f'Список Гали {Galya_list}')
Sasha_list_even = list(filter(lambda x: not x%2, Sasha_list))
print(f'Список Саши c четными монетами {Sasha_list_even}')
Galya_list_even = list(filter(lambda x: not x%2, Galya_list))
print(f'Список Гали c четными монетами {Galya_list_even}')
list_union = [x for x in Sasha_list_even if x in Galya_list_even]
print(f'Общий список {list_union}')
print(sorted(list_union))
# for i in range(len(list_union) - 1):
#     for k in range(len(list_union)-i-1):
#         if list_union[k] > list_union[k+1]:
#             list_union[k+1], list_union[k] = list_union[k], list_union[k+1]
# print(f'Окончательный список {list_union}')
            