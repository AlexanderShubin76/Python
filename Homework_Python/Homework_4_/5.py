# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import get_polynomial as g_p
k_2 = int(input('Задайте натуральную степень k: '))
flag = g_p.get_polynomial(k_2)
# print(flag)
with open('file(task_5-1).txt', 'w') as data:
    data.write(flag)

flag_1 = g_p.get_polynomial(k_2)
# print(flag_1)
with open('file(task_5-2).txt', 'w') as data:
    data.write(flag_1)
f_1 = open('file(task_5-1).txt', 'r')
for line in f_1:
    j = line
    print(j)
data.close()

f_2 = open('file(task_5-2).txt', 'r')
for line1 in f_2:
    z = line1
    print(z)
data.close()
polynomial_1 = j[:-4]
polynomial_2 = z[:-4]
j_list = j.split(' + ')
z_list = z.split(' + ')
