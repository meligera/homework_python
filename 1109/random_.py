from random import choice
import string

# Создание списка
def create_str(width):
    s = ''
    for i in range(width):
        c = choice(string.ascii_lowercase + string.ascii_uppercase)
        s += c
    return (s)


# return [random.choice(string.ascii_letters) for i in range(width)]


def string_(s):
    big = 0
    small = 0
    for c in s:
        if c.isupper():
            big += 1
        else:
            small += 1
        if big > small:
            return 1
        elif big < small:
            return 0
        else:
            return -1


def list_creation(num, s):
    list_ = []
    for i in range(s):
        list_.append(create_str(num))
    return list_


p = list_creation(6, 8)

def percent_creator(s, num):
    s = [create_str(s) for i in range(num)]
    l = ''
    bigger = 0
    smaller = 0
    same_letters = 0
    for el in s:
        if string_(s) == 1:
            bigger += 1
        elif string_(s) == 0:
            smaller += 1
        else:
            same_letters += 1
    ratio_big = (bigger / len(s)) * 100
    ratio_small = (smaller / len(s)) * 100
    ratio_same = (same_letters / len(s)) * 100
    print(ratio_big)
    print(ratio_small)
    print(ratio_same)

def percent_creation(width, num):
    l = [create_str(width) for i in range(num)]
    print (l)
    lenght = len(l)
    c_u = c_l = c_s = 0
    for i in l:
        if i.isupper():
            c_u += 1
        elif i.islower():
            c_l += 1
        else:
            c_s += 1
    p_u = (c_u) / lenght * 100
    p_l = (c_l) / lenght * 100
    p_s = (c_s) / lenght * 100
    print("THE PERCENTAGE OF UPPERCASE LETTERS IN THE STRING IS :", p_u)
    print("THE PERCENTAGE OF LOWECASE LETTERS IN THE STRING IS :", p_l)
    print("THE PERCENTAGE OF SPECIALCASE LETTERS IN THE STRING IS :", p_s)


def cr_list_str(width, num):
    l = [create_str(width) for i in range(num)]
    s = ''
    big = 0
    small = 0
    statb = 0
    stats = 0
    statr = 0
    for el in l:
        s += el
        s += ' '
        for i in el:
            if i.isupper():
                big += 1
            else:
                small += 1
        if big > small:
            statb += 1
            s += '1'
        elif small > big:
            stats += 1
            s += '0'
        else:
            statr += 1
            s += '-1'

        s += ' '
    s += 'Upper ' + str(statb / (statb + stats + statr) * 100) + '% '
    s += 'Lower ' + str(stats / (statb + stats + statr) * 100) + '% '
    s += 'Same ' + str(statr / (statb + stats + statr) * 100) + '%'
    return s

print(cr_list_str(4, 8))


#print(create_str(4))
#print(string_(p))
#print(list_creation(4, 8))
# print(string_(create_str(12)))
