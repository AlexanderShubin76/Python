colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
data.write('\nLINE 12\n')
data.write('LINE 13\n')
data.close()
 
# with open('file.txt', 'a') as data:
#     data.write('line 12\n')
#     data.write('line 23\n')
 
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()