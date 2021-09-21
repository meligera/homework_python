#numbers_ = [5, 2, 12, 1024, 2021, 4, 782, 8970, 7223]
import random
'''
# Ручной способ через функцию
def sort_(numbers_):
    for i in range(len(numbers_)):
        for x in range(i + 1, len(numbers_)):
            if numbers_[i] > numbers_[x]:
                numbers_[i], numbers_[x] = numbers_[x], numbers_[i]
    return numbers_
'''

'''
def lenghtMinMax(x):
    maximum = minimum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum: maximum = i
    return minimum, maximum
'''

def create_list(lenght, minimum, maximum):
    list_=[]
    for i in range (lenght):
        list_.append(random.randrange(minimum, maximum))
    return list_

def create_list_short(lenght, minimum, maximum):
    return [random.randrange(minimum, maximum) for i in range (lenght)]

print(create_list_short(6, 1, 10000))

#print(len(numbers_), lenghtMinMax(numgeneration_namebers_))
# print(sort_(numbers_))
