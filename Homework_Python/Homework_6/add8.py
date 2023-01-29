# Доп 8. Посчитать сумму цифр в вещественном числе
list_1= list(input('Введите вещественное число: '))
summa = sum(map(int,(filter(lambda x: x.isdigit(), list_1))))
print(summa)
