def get_polynomial(k):
    import random
    a = random.randint(0, 100)
    print(f'a = {a}')
    b = random.randint(0, 100)
    print(f'b = {b}')
    c = random.randint(0, 100)
    print(f'c = {c}')
    str_2 = str(b) + 'x'
    if (k == 0 and a+c != 0):
        result = f'{str_2} + {a+c} = 0'
        return result
    elif (k == 0 and a+c == 0):
        result = 'x = 0'
        return result
    elif k == 1 and a+b != 0 and c != 0:
        result = f'{a+b}x + {c} = 0'
        return result
    elif k == 1 and (a+b+c) == 0 or (a+b) == 0:
        result = 'Многочлен не существует'
        return result
    elif k == 1 and a+b != 0 and c == 0:
        result = 'x= 0'
        return result
    elif k >= 2 and a != 0 and b != 0 and c != 0:
        result = f'{a}x^{k} + {str_2} + {c} = 0'
        return result
    elif k >= 2 and a == 0 and b != 0 and c != 0:
        result = f'{str_2} + {c} = 0'
        return result
    elif k >= 2 and a != 0 and b == 0 and c != 0:
        result = f'{a}x^{k} + {c} = 0'
        return result
    elif k >= 2 and a != 0 and b != 0 and c == 0:
        result = f'{a}x^{k} + {str_2} = 0'
        return result
    elif k >= 2 and a == 0 and b == 0 and c != 0:
        result = 'Многочлен не существует'
        return result
    elif k >= 2 and a != 0 and b == 0 and c == 0:
        result = 'x= 0'
        return result
    elif k >= 2 and a == 0 and b != 0 and c == 0:
        result = 'x = 0'
        return result
    else:
        result = 'Ошибка ввода k'
        return result
