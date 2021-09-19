'+7-921-076-59-17'
def validate_number(p):
    if len(p) != 16:
        return False
    if p[0:3] != '+7-':
        return False
    if p[6] != '-' or p[10] != '-' or p[13] != '-':
        return False
    ap = p[3:6] + p[7:10]+p[11:13]+p[14:]
    digits = '0123456789'
    for sym in ap:
        if not sym in digits:
            return False
    return True

my_dict = {}
oper_code = {}

while True:
    n = input('Вас приветствует записная книжка!\n Хотите добавить номер?')
    if n != 'y':
        quit()
    phone = input("Введите номер телефона:")
    if not validate_number(phone):
        print('Oni-chan Baka!')
        quit()
    code_op = phone[3:6]
    number = phone[7:17]
    name = input("Введите имя:")
    my_dict[name] = code_op + ' ', number
    print(my_dict)

add_to_book()


# Цикл запускает новый номер 1)имя, 2)телефон, 3)q - выход из цикла
