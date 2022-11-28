
def write(data):
    l = ['Фамилия ', 'Имя ', 'Телефон ', 'Описание ']
    data = []
    for i in range(len(l)):
        data.append(input(l[i]))
    with open('data.txt', 'a') as file:
        file.write('\n' + " ".join(map(str, data)))
        file.close()

    l = ['Фамилия ', 'Имя ', 'Телефон ', 'Описание ']
    data = []
    for i in range(len(l)):
        data.append(input(l[i]))
    with open('data.csv', 'a') as file:
        file.write('\n' + " ".join(map(str, data)))
        file.close()

