# Данный модуль отвечает за взаимодействие между модулем model и действиями пользователя, полученными
# в модуле view. Тут описаны 2 метода. Один для экспорта данных из телефонного справочника
# "phone_book.p" # в файлы формата .txt или .csv. Другой метод нужен для внесения изменения в телефонный справочник.

import model as md
import view

def create_phone_book(): # Вносим изменения в телефонную книгу
    for i in md.phone_book.items():
            print(f'{i}\n')
    arg = view.view_phone_book()
    s = 1
    while s !=0:
        if arg == 0:
            return

        if arg == 1:
            a,b,c,d,e,i = view.new_id()
            md.add_id(a,b,c,d,e,i)

        if arg == 2:
            md.del_id(view.remove_id())
        
        if arg == 3:
            j,k,l,m,n,o = view.rerecord_id()
            md.add_id(j,k,l,m,n,o)

        for i in md.phone_book.items():
            print(f'{i}\n')

        s = view.select_action()

def export_format(): # Экспортируем данные телефонной книги в нужный нам формат
    for i in md.phone_book.items():
        print(f'{i}\n')
        
    n = view.choice_export_format()
    if n == 0: # Не экспортируем данные
        return
    if n == 1:
        md.export_txt_format('phone_book.txt')
    if n == 2:
        md.export_csv_format('phone_book.csv')
    

