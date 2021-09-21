class Summator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def return_sum(self):
        return self.a + self.b


s = Summator(123, 377)
s.return_sum()

class Car():
    def __init__(self):
        pass

    def what_is_this(self):
        print('I am a car!')


class Pink_car(Car):
    def what_color(self):
        print('Pink!')


class Person():
    def __init__(self, name):
        self.name = name

class Student(Person):
    homework = 0
    kn = 0
    def get_kn(self):
        self.kn += 1
    def get_homework(self, n):
        self.homework += n
    def do_homework(self):
        if self.homework > 0:
            self.homework -= 1
            self.kn += 1
        else:
            print('Nothing to do')

class Teacher(Person):
    work = 0
    def give_kn(self, *pupils):
        for pupil in pupils:
            pupil.get_kn()
            self.work += 1
    def give_homework(self, *pupils):
        for pupil in pupils:
            pupil.get_homework(n)
            work += 1

t = Teacher('Albert Andreevich')
p = Student('Masha')

t.give_kn(p)
t.give_homework()
p.get_homework(2)
p.do_homework()
p.do_homework()
p.do_homework()
print(p.kn)
print(p.homework)




'''
    def exclaim(self):
        print('I am a human, my name is:', self.name)

    def __del__(self):
        print('Object was deleted:', self)


class Student(Person):
    def exclaim(self):
        print('I am a human, my name is:', self.name, 'but I wanna sleep more!')








#p = Person('Vasya')
#s = Student('Vanya')
#print(isinstance(p, Student))
#print(issubclass(Student, Person))

# pink_car = Pink_car()
# pink_car.what_is_this()
# pink_car.what_color()
'''