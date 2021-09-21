import string

alph = [chr(i) for i in range(ord('a'), ord('z') + 1)]

#for i in range(ord('a'), ord('z') + 1):
#    print(chr(i))

alphabet = list(string.ascii_lowercase)

#def list_def_for(alph):
#  for i in range(ord('a'), ord('z') + 1):
#    print(chr(i))

def list_def_while(l):
  i = 0
  while i < len(l):
    print(l[i])
    i += 1

#list_def_while(alph)


def dec(leng):
    def new_leng(*args, **kwargs):
        print('Running... : ', leng.__name__)
        print('Arguments: ', args)
        print('Keywords: ', kwargs)
        result = leng(*args, **kwargs)
        print('Result: ', result)
        return result

    return new_leng


decorator_ = dec(list_def_while)

decorator_(alph)

#print(alph)
#print(alphabet)
