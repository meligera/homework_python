import string

storage_ = {"name": 'Maria', "age": "23", "occupation": "Carpenter", "gender": 'female'}


def get_value(d, k):
    if k in d.keys():
        return d[k]
    else:
        return -1


def get_value2(d, k):
    return d.get(k, -1)


def ascii_upper():
    characters = {}
    for i in range(65, 91):
        characters[chr(i)] = i
    return characters


def ascii_upper1():
    return {chr(i): i for i in range(65, 91)}


s = 'aabbcde'

import string


def counter_letters(s):
    return {e: s.count(e) for e in string.ascii_lowercase}

# d.clear() - удаляет все элементы словаря
# d.pop() - удаляет и возвращает
# d.items - [(k,v), (k1,v1)...
# d.update(d1)
