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

list_def_while(alph)

#print(alph)
#print(alphabet)
