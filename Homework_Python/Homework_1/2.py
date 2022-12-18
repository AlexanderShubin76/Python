# 2. Напишите программу для проверки истинности утверждения:
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения:
# not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])
# для всех значений предикат.
def check_truth(x,y,z):
    if not(x or y or z) == (not x and not y and not z):
        print('True')
    else:
        print('False')
num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
num3 = int(input('Введите число 3: '))
check_truth(num1, num2, num3)