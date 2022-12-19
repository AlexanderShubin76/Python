# import Hello_python as h

# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print (new_string('!', 5))
# print (new_string('!'))
# print (new_string(4))

# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))
# print(concatenatio(1, 2, 3, 4))

# Кортежи
# a = (3, 4)
# print(a)
# print(a[-1])

# colors = ['red', 'green', 'blue']
# t = tuple(colors)
# print(type(t))
# t = (['red', 'green', 'blue'])
# for e in t:
#     print(e, end = ' ')

# t = tuple (['red', 'green', 'blue'])
# red, green, blue = t
# print(f'r: {red} g: {green} b:{blue}')

# Словари
# dictionary = {}
# dictionary = \
# {
#     'up' : '|',
#     'left' : '-',
#     'down' : '|',
#     'right' : '-'
# }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)
# for v in dictionary.values():
#     print(v)
# for v in dictionary:
#     print(dictionary[v])
# for v in dictionary: # распечатать ключ
#     print(v)

# del dictionary['left'] # удаление элемента
# dictionary['up'] = 'up'
# print(dictionary['up'])

# for item in dictionary:
#     print(f'{item}: {dictionary[item]}')

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# colors.add('gray')
# colors.remove('red') # будет ошибка
# colors.discard('red') # удаление без ошибки
# colors.clear() # очистить множество

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)

# q = a\
#     .union(b) \
#     .difference(a.intersection(b))

# s = frozenset(a) # замороженное множество

# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e, end = ' ')

# print()

# for e in list2:
#     print(e, end = ' ')

list1 = [1, 2, 3, 4, 5]
# print(len(list1))
# print(list1.pop()) # удаляет последний элемент по умолчание. Метод удаляет по индексу
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.insert(1, 11)) #вставить элемент
# print(list1)
print(list1.append(11)) # вставить в конец
print(list1)