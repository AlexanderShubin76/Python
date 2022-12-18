# 1. Стоимость строки

# Дана строка текста. Напишите программу для подсчета стоимости строки,
#  исходя из того, что один любой символ (в том числе пробел) стоит
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести стоимость строки.

# Тестовые данные
# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.
# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.

text = input('Введите текст: ')
cost = len(text) * 0.6
rub = int(cost)
cop = int(round((cost - rub),1) * 100)
print(f'{rub} р. {cop} коп.')