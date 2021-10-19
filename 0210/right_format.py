file = input('Which file?')
try:
    grade = int(input('Passing grade:'))
except Exception as err:
    print('C`mon, enter a number not characters!', err)
    quit()
try:
    f = open(file, 'r')
except Exception as err:
    print('No such file, baka!', err)
    quit()

lines = f.readlines()
for line in lines:
    p = line.split()
    b = p[-1]
    if b == 'a':
        b = 5
    if b == 'b':
        b = 4
    if b == 'c':
        b = 3
    if b == 'd':
        b = 2
    try:
        c = int(b)
    except Exception as err:
        print('The value in file is not an int!', err)
    if c <= grade:
        print(p [0:2], b)


