import keyword
import random


class Person():
    def __init__(self, name):
        self.name = name

    def talk(self, text):
        print(self.name, ': ', text)

p = Person('Siri')
p2 = Person('Алиса')

common_list = ['Hello', 'See ya later', 'How are you?', 'How have you been?', 'How’s your family?', 'Pretty good.',\
               "Can’t complain", 'Thanks a lot.', 'I really appreciate it.', 'I’m not really sure.', 'I’m single.',\
               'I’m divorced', 'Would you like a drink?']

n = 0
while n < 5:
    p.talk(random.choice(common_list))
    p2.talk(random.choice(common_list))
    n += 1