# 2. Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
a = ( "a", 'b', '2', '3' ,'c')
# list_numbers = list(filter(lambda x: x.isdigit(), a))
# list_letters = list(filter(lambda x: not x.isdigit(), a))
# print(list_numbers)
# print(list_letters)
b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)