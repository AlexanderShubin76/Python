# Данный модуль отвечает за взаимодействие между модулем model и действиями пользователя, полученными
# в модуле view. Тут описан 1 метод для работы со словарем workers.

import model as md
import view

def operations_with_workers(): # Вносим изменения в телефонную книгу
    view.print_workers()
    arg = view.show_menu()
    while arg != 9:
        
        if arg == 1: # Ищем сотрудника по id
            id = view.get_id()
            md.search_worker(id)
        
        if arg == 2: # Делаем выборку сотрудников по професии
            position = view.get_position()
            md.search_post(position)    
        
        if arg == 3: # Делаем выборку сотрудников по зарплате
            a,b = view.get_salary()
            md.search_salary(a,b)

        if arg == 4: # Добавляем данные о новом сотруднике
            a,b,c,d,e,i = view.new_id()
            md.add_id(a,b,c,d,e,i)
            view.print_workers()

        if arg == 5: # Удаляем записи о сотруднике
            md.del_id(view.remove_id())
            view.print_workers()

        if arg == 6: # Изменяем записи о сотруднике
            j,l,m,n,o = view.rerecord_id()
            md.rewrite_id(j,l,m,n,o)
            view.print_workers()

        if arg == 7: # Экспортируем словарь с сотрудниками в .json формат
            md.export_json_format('workers.json')
            
        if arg == 8:
            md.export_csv_format('workers.csv') # Экспортируем словарь с сотрудниками в .csv формат
        
        arg = view.show_menu()


    

