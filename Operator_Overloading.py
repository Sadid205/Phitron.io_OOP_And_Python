class Sum:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __add__(self,other): # here 
        return self.a+other.a,self.b+other.b


my_sum = Sum(5,6)
your_sum = Sum(4,5)

# here '+'operator is overloaded the Sum class.
print(my_sum+your_sum)
# here is the output (9,11)