# 3)Вводится слово. Переменной msg присвоить строку "палиндром", если введенное слово является палиндромом
# (одинаково читается и вперед и назад), а иначе присвоить строку "не палиндром".
# Проверку проводить без учета регистра.
# Программу реализовать с помощью тернарного условного оператора.
# Значение переменной msg отобразить на экране.

# Sample Input:
# Казак
# Sample Output:
# палиндром

str = input('Введите слово: ')
str_mod = str.lower()
result = print('Число является палиндромом') if str_mod[:] == str_mod[::-1] else (print('Число не является палиндромом'))