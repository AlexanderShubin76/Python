# 4)Создать текстовый файл, записать в него построчно
# данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
# with open('file.txt', 'w') as data:
#     data.write(input('Введите данные: '))
#     data.write('\n')
#     data.write(input('Введите данные: '))
#     data.write('\n')
data = open('file.txt', 'w')

while True:
    a = input()
    data.write(a)

    if a == '':
        break