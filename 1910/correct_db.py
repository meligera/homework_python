import sqlite3
def showmenu(level):
    if level == 1:
        return '1. New 2. Work with DB 0. Exit'
    else:
        return '1.Select 2. Update. 3 Delete 0. Return to menu'
menu_level = 1
connection = None
cursor = None
while True:
    answer = input(showmenu(menu_level))
    if menu_level == 1:
        if answer == '0':
            break
        elif answer == '2':
            menu_level = 2
        elif answer == '1':
            path = input('Locate the DB:')
            if connection:
                connection.close()
            if cursor:
                cursor.close()
            connection = sqlite3.connect(path)
            cursor = connection.cursor()
    elif menu_level == 2:
        answer = input() + (showmenu(2))
        if answer == '1':
            select = input('SELECT: ')
            fr = input('FROM: ')
            where = input('WHERE: ')
            if cursor:
                com = 'SELECT %s FROM %s WHERE %s;' %(select, fr, where)
                cursor.execute(com)
                print(cursor.fetchall())
        elif answer == '0':
            menu_level == 1