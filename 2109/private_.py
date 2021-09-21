class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_all(self):
        return self.__name, self.__age

    def set_all(self, new_name, new_age):
        self.__name = new_name
        self.__age = new_age
        return self.__name, self.__age


st = Person('Michael', 23)
print(st.set_all('Rob', 17))
