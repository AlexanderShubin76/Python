# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file(task_5-1).txt', 'r') as data:
    for line in data:
        p_1 = line
        print(p_1)

with open('file(task_5-2).txt', 'r') as data:
    for line in data:
        p_2 = line
        print(p_2)

p_1_list = p_1.split(' + ')
p_2_list = p_2.split(' + ')

str_3 = str(int(p_1_list[-1]) + int(p_2_list[-1]))

p_1_list_1 = p_1_list[1]
p_2_list_1 = p_2_list[1]
str_2 = str(int(p_1_list_1[:-1]) + int(p_2_list_1[:-1])) + 'x'

p_1_list_0 = p_1_list[0]
p_2_list_0 = p_2_list[0]
if (p_1_list_0[-1] == p_2_list_0[-1]):
    str_1 = str(int(p_1_list_0[:-3]) + int(p_2_list_0[:-3])) + p_1_list_0[-3:]
if (p_1_list_0[-1] != p_2_list_0[-1]):
    str_1 = f'{p_1_list[0]} + {p_2_list[0]}'
result = f'{str_1} + {str_2} + {str_3}'
print(result)

with open('file(task_5-3).txt', 'w') as data:
    data.write(result)
