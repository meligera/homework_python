class Car:
    type = 'Car'

    def __init__(self, speed):
        self.speed = speed


class Mazda(Car):
    model = 'Mazda'

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed


class Porsche(Car):
    model = 'Porsche'

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed


class Lamborghini(Car):
    model = 'Lamborghini'

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed


pos_l = 0
pos_p = 0
pos_m = 0
finish_race = 1000
l = Lamborghini(250)
p = Porsche(260)
m = Mazda(238)
while pos_m < finish_race and pos_p < finish_race:
    pos_m += m.speed
    pos_p += p.speed
if pos_p > pos_m:
    print('Porsche')
if pos_m > pos_p:
    print('Mazda')