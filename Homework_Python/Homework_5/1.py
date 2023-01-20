# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_list = input('Введите текст: ').split()
result = list(filter(lambda x: 'абв' not in x, my_list))
print(*result)
