def correct_number():
    number = input('номер +7 код номер без пробелов : ')
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 11:
           return number
        print('не корректный ввод')
        number = input('номер +7 код номер без пробелов : ')

number = correct_number()
