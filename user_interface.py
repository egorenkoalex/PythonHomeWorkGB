import close
import write
import search
import scan
import csv



def readfile(filename):
    # чтение файла при запуске
    return open(filename).read().split('\n')
        

data = readfile('data.txt') # При запуске программы (скрипта), она должна считывать содержимое

dict_command = {'1' : readfile, '2' : readfile, '3' : scan.scan, '4' : search.search,\
     '5' : write.write, '6' : close.close} # словарь команд, в значениях функции их исполняющие
 
print('''Команды для работы со справочником:
    Какой файл открыть: csv-1, txt-2
    Просмотр всех записей справочника:  - 3
    Поиск по справочнику -4
    Добавление новой записи - 5
    Завершение работы- 6''')
 
while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')





