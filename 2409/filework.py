f = open('port.txt', 'r')
lines = f.readlines()
lines = [line[:-1] for line in lines]
dict_ = {'ip': lines[2][:-1], 'port': int(lines[4][:-1])}
d = {lines[1]:lines[2], lines[3]: int(lines[4])}
print(d)
f.close()