# 3)
# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы.
 
# Формат входных данных
# В первой строке подаётся число n
# n – количество холодильников. В последующих n строках вводятся строки, содержащие латинские
# строчные буквы и цифры, в каждой строке от 5 до 100 символов.
 
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.
# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# n = int(input('Введите количество холодильников: '))
# list = []
# for i in range(n):
#     list.append(input('Введите код холодильника: '))
    
# for i in range(n):
#     if len(list[i]) < 5 or len(list[i]) > 100:
#         continue
    # strk = ''
    # for k in list[i]:
    #     if (k == 'a' or k == 'n' or k == 't' or k =='o' or k == 'n'):
    #         strk += k
    # if strk == 'anton':
    #     print(i+1, end=' ')
    # sym = 'a'
    # for k in list[i]:
    #     if (k == 'sym'):
    #         sym = 'n'
    #         continue
    #     elif (k == 'sym'):
    #         sym = 't'
    #         continue
    #     elif (k == 'sym'):
    #         sym = 'o'
    #         continue
    #     elif (k == sym):
    #         sym = 'n'
    #         continue
    #     elif (k == sym):
    #         print(i+1, end=' ')
    #         break
    # else:
    #     break
n = int(input())
list1 = []
for i in range(n):
    a = input()
    if 'a' in a:
        a = a[a.find('a'):]
        if 'n' in a:
            a = a[a.find('n'):]
            if 't' in a:
                a = a[a.find('t'):]
                if 'o' in a:
                    a = a[a.find('o'):]
                    if 'n' in a:
                        list1.append(i + 1)
print(*list1)