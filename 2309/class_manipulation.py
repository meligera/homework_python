class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Student(Person):
    def __init__(self, name, age, height, weight, study):
        super().__init__(name, age, height, weight)
        self.study = study

    def get_s(self):
        return self.name, self.age, self.height, self.weight, self.study


# t = Student('Masha', 18, 178, 63, 5)
# print(t.get_s())

class Name:
    def __init__(self, name):
        self.__hidden_name = name

    def get_name(self):
        print('Getter')
        return self.__hidden_name

    def set_name(self, name):
        print('Setter')
        self.__hidden_name = name

    name = property(get_name, set_name)


n = Name('Madonna')
print(n.get_name())
n.set_name('Taylor')
print(n.get_name())
