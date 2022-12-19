# 5. Реализуйте алгоритм перемешивания списка.
from random import randint
list_1 = []
 
for i in range (10):  
    list_1.append(randint(-100, 100))
print('list_1 =', ''.join(str(list_1)))
for i in range (8):
    (list_1[i], list_1[i+2]) = (list_1[i+2], list_1[i])
 
print('Вид списка list_1 после перемешивания ', ''.join(str(list_1)))
