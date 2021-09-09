names = ['Tenigin Albert Andreevich', 'Volkov Stephan Sergeevich', 'Parusova Anastasia Sergeevna',
         'Mokrushev Genadiy Petrovich', 'Kozirev Alexandr Albertovich']
name = 'Tenigin Albert Andreevich'


def initials(name):
    x = name.split()
    return x[0] + ' ' + x[1][0:1] + '. ' + x[2][0:1] + '.'


def initials_more(names):
    return [initials(name) for name in names]

# Импортирую функцию рандома, начинаю перетасовку элементов списка
from random import shuffle
shuffle(names)

# Дублирую список простым умножением
print(initials_more(names * 3))
