# Here is the parent class Person.
class Person:
    def __init__(self,name,age,height,weight,gender) -> None:
        self.Name = name
        self.Age = age
        self.Height = height
        self.Weight = weight
        self.Gender = gender
    def __repr__(self) -> str:
        return (f'Name:{self.Name},Age:{self.Age},Height:{self.Height},Weight:{self.Weight},Gender:{self.Gender}')

# Here is the subclass Student.
# This Student class inherit the Person class.
class Student(Person):
    def __init__(self, name, age, height, weight, gender,roll,address,email) -> None:
        super().__init__(name, age, height, weight, gender) # Superclass constructor
        self.Roll = roll # Student class specific attributes
        self.Address = address # Student class specific attributes
        self.Email = email # Student class specific attributes
    def __repr__(self) -> str:
        return f"{super().__repr__()},Roll:{self.Roll},Address:{self.Address},Email:{self.Email}"

my_student = Student('Abdullah Al sadid',22,'5.7 inch','62 kg','Male',34032,'Taherhuda/Horinakundu/Jhenaidah','rongdhonu5858@gmail.com',)
print(my_student)