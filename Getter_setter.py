class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.__age = age
    
    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def modify_age(self,new_age):
        self.__age = new_age



Tamim = Person('Tamim',38)
print(Tamim.get_age)
Tamim.modify_age = 40
print(Tamim.get_age)