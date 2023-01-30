# Данный модуль отвечает за взаимодействие между модулем model и действиями пользователя, полученными
# в модуле view. Тут описан 1 метод для работы со словарем workers.

import model as md
import view

def operations_with_workers(): # Вносим изменения в телефонную книгу
    print_workers()
    arg = view.show_menu()
    while arg != 9:
        
        if arg == 1:
            id = get_id()
            search_worker(id)
        
        if arg == 2:
            md.del_id(view.remove_id())
        
        if arg == 3:
            j,k,l,m,n,o = view.rerecord_id()
            md.add_id(j,k,l,m,n,o)

        print_workers()
        
        arg = view.show_menu()


def create_workers(): 
    print_workers()
    # arg = view.show_menu()
    while arg != 9:
        
        if arg == 1:
            id = get_id()
            search_worker(id)
        
        if arg == 2:
            md.del_id(view.remove_id())
        
        if arg == 3:
            j,k,l,m,n,o = view.rerecord_id()
            md.add_id(j,k,l,m,n,o)

        print_workers()
        
        # arg = view.show_menu()
        

def export_format(): # Экспортируем данные телефонной книги в нужный нам формат
    for i in md.workers.items():
        print(f'{i}\n')
        
    n = view.choice_export_format()
    if n == 0: # Не экспортируем данные
        return
    if n == 1:
        md.export_txt_format('workers.txt')
    if n == 2:
        md.export_csv_format('workers.csv')
    

