# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open('file_1.txt', 'w') as data:
    data.write('AAAAAAAAAAAAAAAAAABBBFFFFFFFFFFFFFFFFFFFFFGGEEEEEEEEEEEEEEEEEEDGDS')
with open('file_1.txt', 'r') as data:
    text = data.read()
print(text)
def rle_fun(txt):
    rle_text = ''
    count = 1
    for i in range(1, len(txt)):
        if txt[i] == txt [i-1]:
            count +=1
        else:
            rle_text += (str(count) + txt[i-1])
            count = 1
        if i == len(txt) -1:
            rle_text += (str(count) + txt[i])
        
    return rle_text
rle_txt = rle_fun(text)
print(rle_txt)

with open('rle_file.txt', 'w') as data_1:
    data_1.write(rle_txt)

with open('rle_file.txt', 'r') as data_2:
    compressed_text = data_2.read()

def recover_file(rle_str):
    new_string = ''
    y = len(rle_str)
    x = 1
    while( 0<x<y):
        if rle_str[x].isalpha():
            new_string += (int(rle_str[:x]) * rle_str[x])
            rle_str = rle_str[x+1:]
            y -= x+1
            x = 1
        else:
            x+=1
    return new_string
yx = recover_file(compressed_text)
print(yx)
with open('recover_file.txt', 'w') as data_3:
    data_3.write(yx)
