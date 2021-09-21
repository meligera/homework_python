class Field():
    __pos_hare = 0
    __pos_tort = 0

    def __init__(self, step_h, step_t, field):
        if step_h <= step_t:
            print('Turtles can`t be faster')
            quit()
        self.__step_h = step_h
        self.__step_t = step_t
        self.__field = field

    def step(self):
        hare_new_pos = self.__pos_hare + self.__step_h
        if hare_new_pos > self.__field:
            hare_new_pos -= self.__field
        self.__pos_hare = hare_new_pos
        tort_new_pos = self.__pos_tort + self.__step_t
        if tort_new_pos > self.__field:
            tort_new_pos -= self.__field
        self.__pos_tort = tort_new_pos

    def get_pos_hare(self):
        return self.__pos_hare

    def get_pos_tort(self):
        return self.__pos_tort


f = Field(5, 2, 13)
i = 0
b = 0
first_meet = 0
while i < 44:
    f.step()
    i += 1
    if f.get_pos_hare() == f.get_pos_tort():
        b += 1
        print('They met after:', i - first_meet)
        first_meet = i
print('They collided :', b, 'times')