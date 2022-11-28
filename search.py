
def search(data):
    # Поиск по справочнику.
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('Нет такой записи')