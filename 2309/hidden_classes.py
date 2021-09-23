class Counter():
    def __init__(self):
        self.__counter_value = 0

    def get_count(self):
        return self.__counter_value

    def count(self):
        self.__counter_value += 1

    def count_to_zero(self):
        return self.__counter_value == 0


# s = Counter()
# s.count()
# s.count()
# print(s.get_count())
import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Parent(Person):
    def __init__(self, name, age, hair, eyes):
        super().__init__(name, age)
        self.hair = hair
        self.eyes = eyes


class Child(Person):
    def __init__(self, name, age, parent1, parent2):
        super().__init__(name, age)
        hair_1 = parent1.hair
        hair_2 = parent2.hair
        hair_all = [hair_1, hair_2]
        self.hair = random.choice(hair_all)
        eyes_1 = parent1.eyes
        eyes_2 = parent2.eyes
        eyes_all = [eyes_2, eyes_1]
        self.eyes = random.choice(eyes_all)


parent1 = Parent('Michael', 29, 'blonde', 'green')
parent2 = Parent('Sara', 27, 'brown', 'blue')
child1 = Child('John', 3, parent1, parent2)
print(child1.eyes)
