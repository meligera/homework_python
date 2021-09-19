my_list = []

while True:
    value = input('Input checker: ')
    if value == 'q':
        print('Thank you for using Input checker')
        quit()
    index1 = int(input('Enter index: '))
    try:
        my_list[index1] = value
    except IndexError as err:
        print('Wrong index', err)
    except TypeError as err:
        print('Wrong type of data')
    except ZeroDivisionError as err:
        print('Don`t divide by zero!')
    else:
        print('That was okay!')
    finally:
        print('Error display test complete')

# 1) TypeError: (обращаемся не к тому типу данных)
# 2) IndexError: l[2], <l[0, 1]>
# 3) ZeroDivisionError: (попытка разделить на ноль)
