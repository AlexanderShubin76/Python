# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open('file_1.txt', 'r') as data:
    text = data.read()
print(text)
def rle_fun(txt):
    rle_text = ''
    count = 1
    for i in range(len(txt)):
        if not i:
            rle_text = str(count) + txt[0]
        else:
            if txt[i] != txt [i-1]:
                count = 1
                rle_text += (str(count) + txt[i])

            else:
                count+=1
                rle_text = rle_text[:-1-len(str(count))]
                rle_text += (str(count) + txt[i])
    return rle_text
rle_txt = rle_fun(text)
print(rle_txt)

with open('rle_file.txt', 'w') as data_1:
    data_1.write(rle_txt)

with open('rle_file.txt', 'r') as data_2:
    compressed_text = data_2.read()
# print(int(compressed_text[:2]) * compressed_text[2])
# print(compressed_text[:2].isdigit())
def recover_file(rle_str):
    new_string = ''
    y = len(rle_str)
    for x in range(y):
        if x!=0:
            if rle_str[x].isalpha():
                new_string += (int(rle_str[:x]) * rle_str[x])
                rle_str = rle_str[x+1:]
                y -= x+1
                print(y)
                x -= x+1
                print(x)

                print(new_string)
                print(rle_str)
    return new_string
yx= recover_file(compressed_text)
print(yx)
# with open('recover_file.txt', 'w') as data_3:
#     data_3.write(y)
