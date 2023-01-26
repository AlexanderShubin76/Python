# 1. Напечатать строку в одну линию - C:\WINDOWS\System32\drivers\etc\nst
a = 'C:\WINDOWS\System32\drivers\etc\nst'.split('\n')
print(f'{a[0]}\ n{a[1]}'.replace(' ', ''))
