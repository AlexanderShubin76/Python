# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list_2 = []
# path = 'C:\Users\pastu\OneDrive\Desktop\Курс по питон гик брейнс\Python_begining\Lectures\Lecture_3\text.txt'
# with open(path, 'r') as data:
#     for line in data:
#         for j in line:
#             list_2.append(j)
# def f(x):
#     return x **2
# list = [(x, f(x)) for x in list_1 if x % 2 == 0]
# list_3 = [(x, f(x)) for x in list_2 if x % 2 == 0]
# print(list)
# print(list_3)

path = 'C:/Users/pastu/OneDrive/Desktop/Курс по питон гик брейнс/Python_begining/Lectures/Lecture_3/text.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data!= '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1]

out = []

for e in numbers:
    if not e %2:
        out.append((e,e **2))
print(out)