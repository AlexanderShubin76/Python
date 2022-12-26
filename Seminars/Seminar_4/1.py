# 1. Больше предыдущего

# На вход программе подается строка текста из натуральных чисел.
# Из неё формируется список чисел.
# Напишите программу подсчета количества чисел,
# которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом. 

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.

# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.

# Те v  стовые данные 
# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# 4
# Sample Input 2:
# 1 1 3 2 2 1 1 1 1
# Sample Output 2:
# 1
# Sample Input 3:
# 5 4 3 2 1
# Sample Output 3:
# 0

str = input('Введите последовательность натруральных чисел, разделенных пробелом: ')
list = str.split(' ')
count = 0
for i in range(len(list)-1):
    if(list[i+1]> list[i]):
        count +=1
print(f'Количество элементов списка, больших предыдущего равно "{count}"')
