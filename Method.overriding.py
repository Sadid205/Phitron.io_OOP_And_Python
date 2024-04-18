class Override:
    def __init__(self,name,age,weight) -> None:
        self.name = name
        self.age = age 
        self.weight = weight
    def my_age(self):
        return f'I am Override Class and my age is :{self.age}'


class Overrided_class(Override):
    def __init__(self, name, age, weight,male_age) -> None:
        super().__init__(name, age, weight)
        self.male_age = male_age

    def my_age(self): # here my_age method is override of its super class my_age.
        return f'I am Overrided Class and my male_age is :{self.male_age}'



A = Override('Sakib',38,70)
print(A.my_age())
B = Overrided_class('Mushfiq',37,65,45)
print(B.my_age())
