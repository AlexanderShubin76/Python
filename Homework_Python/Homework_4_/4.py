# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import get_polynomial as g_p
k_1 = int(input('Задайте натуральную степень k: '))
flag = g_p.get_polynomial(k_1)
print(flag)
with open('file(task_4).txt', 'w') as data:
    data.write(flag)
