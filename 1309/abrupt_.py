# Extension extraction
'''
file = 'python.py', 'minecraft.jar', 'word.exe'

def split_(file):
    l = file.split('.')
    if len(l)<2:
        return 'Invalid'
    else:
        return '.'+l[-1]

print(split_(file))
'''
# Convertion of seconds into time format
'''
x = input('Enter the amount of seconds:')
x = int(x)


def convert_t(seconds):
    days = seconds // (24*60*60)
    seconds = seconds% (24*60*60)
    hours = seconds // (24*60)
    seconds = seconds% (24*60)
    minutes = seconds // 60
    seconds = seconds%60
    return str(days)+':'+str(hours)+':'+str(minutes)+':'+str(seconds)


print(convert_t(x))
'''
# Palindrome function
'''
x = input('Enter a word: ')

def is_palindrome(l):
    return l == l [::-1]
b = is_palindrome(x)
if b:
    print('It\'s a palindrome!')
else:
    print('Ordinary word')
'''
# Number duplication
'''
n = int(input('Enter the number: '))
t = str(n)
t1 = t + t
t2 = t + t + t
all = n + int(t1) + int(t2)

print('The result is:', all)
'''
# Generation function
import random

def generation_name(num, minimum, maximum):
    i = 0
    while i < num:
        yield random.randrange(minimum, maximum)
        i += 1
list_ = [i for i in generation_name(30, 0, 40)]

print(list_)
