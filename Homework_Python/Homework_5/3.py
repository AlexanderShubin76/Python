# 3. Создайте программу для игры в ""Крестики-нолики"".

mas = ['* * *'.split() for x in range(3)]
for i in range(len(mas)):
    for x in range(len(mas[i])):
        print(*mas[i][x], end ='  ')
    print()
# mas = [list(map(int, input().split())) for i in range(int(input()))]
# print(mas)
