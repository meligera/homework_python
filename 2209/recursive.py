def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def dividers(n, div=1, all_divs=[]):
    if n == div:
        all_divs.append(div)
        return all_divs
    if n == div/2:
        return n
    elif div < n:
        if n % div == 0:
            all_divs.append(div)
        return dividers(n, div=div+1, all_divs=all_divs)
    else:
        print('Wrong n')


def order(n):
    res = [int(x) for x in str(n)]
    return res

def order1(n):
    if n < 10:
        return [n]
    return order1(n//10)+[n%10]




#1) вывести 1 разряд
#2) вызвать эту функцию со всем кроме 1 разряда

print(order1(57822))
