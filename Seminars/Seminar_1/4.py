# 1. Напишите программу, которая будет на вход принимать
# число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
def output(num1):
    if (num1 >= 0):

        # list = []
        # n = num1*2+1
        # for i in range(-num1, num1+1):
        #     list.append(i)
        # print(''.join(str(list)))
        a = - num1
        while (a<=num1):
            if (a==num1):
                print(a)
                break
            print(f'{a} , ', end ="")
            a +=1
    else:
        print('Введено отрицательное число')
print('Введите положительное число:')
output(int(input()))
