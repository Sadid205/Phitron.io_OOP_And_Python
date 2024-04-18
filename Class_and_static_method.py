class Class_and_static:
    def __init__(self,name,age,height) -> None:
        self.name = name
        self.age = age
        self.height = height
    
    @staticmethod
    def multiply(a,b):
        # print(self.name)  Here you can't use the instance attribute of 
        # this class
        return a*b
    @classmethod
    def summation(self,a,b):
        print(self.name) # Here you can use the instance attribute of this class
        return a+b
        


instance1 = Class_and_static('Sadid',22,"5.8")
instance2 = Class_and_static('Sakib',38,'6')
print(instance1.multiply(2,3))
print(instance2.summation(40,50))