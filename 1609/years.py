# Программа принимает число месяц год и проверяет существует ли такая дата
import datetime
while True:
    date_ = input('Input the date in standard format DD/MM/YY: ')
    if date_ == ('q'):
        print('Oni-chan, goodbye!')
        quit()

    day , month, year = date_.split('/')

    d = int(day)
    m = int(month)
    y = int(year)

    def checkfake(d):
        if not(0 < d < 32):
            print('Oni-chan Baka!')
            quit()
    def checkmonth(m):
        if not(0 < m < 13):
            print('Oni-chan Baka!')
            quit()
    def checkyear(y):
        if not(y > 0):
            print('Oni-chan Baka!')
            quit()
    def february(d, m):
        if m == 2 and d == 29:
            n = input('Это високосный год?')
            if n != 'y':
                print('Oni-chan Baka!')
                quit()

    def April(d):
        if m==1 and 0 < d < 31:
            print('Oni-chan Baka!')
            quit()
    def June(d):
        if m==1 and 0 < d < 31:
            print('Oni-chan Baka!')
            quit()
    def September(d):
        if m==1 and 0 < d < 31:
            print('Oni-chan Baka!')
            quit()

    def November(d):
            if m == 1 and 0 < d < 31:
                print('Oni-chan Baka!')
            quit()


    checkfake(d)
    checkmonth(m)
    checkyear(y)
    february(d, m)

    print('Oni-chan, you are the best! UwU', day, month, year)