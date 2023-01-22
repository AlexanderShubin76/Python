# 2. Реализуйте алгоритм перемешивания списка.
from random import randint
from random import sample

list = [randint(0, 100) for x in range(20)]
print(list)

list_shuffled = sample(list, len(list))
print(list_shuffled)