class Student:
    def __init__(self,age,email,id) -> None:
        self.Age = age # Public (These members are accessed from anywhere)
        self._Email = email # Protected (In C++ and JAVA are those members of the class that cant not be accessed outside the class but can be accessed from within the class and its subclasses.To accomplish this in Python, just follow the convention by pre fixing the name of the member by a single underscore"_")
        self.__Student_id = id # Private (These members can not be accessed outside the class nor by any base class) To define Private members in Python you have to use "__" double underscore before a member name.
    
    def __repr__(self) -> str:
        return f'{self.__Student_id}' # You can access from this class but can not access outside the class.

 
my_student = Student(44,'sadid9494@gmail.com',9932)
print(my_student.Age) # This code will print the Student Age
print(my_student._Email) #
print(my_student)
print(my_student.__Student_id) 
# If you want to access outside the class then here is the Error,
# Traceback (most recent call last):
#   File "D:\0.Phitron\Modules\OOP and Python\Module 6.5 Python Week 2 Practice Day 01 date_15_4_24\encapsulation.py", line 15, in <module>#     print(my_student.__Student_id)
#           ^^^^^^^^^^^^^^^^^^^^^^^
#AttributeError: 'Student' object has no attribute '__Student_id'
                                     