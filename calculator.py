# task for you !!!

class Calculator:
    brand = 'Casio MS990'
    def add(self,num1,num2):
        return num1+num2
    def deduct(self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        return num1//num2

calc = Calculator()

adding = calc.add(6,5)
deducting = calc.deduct(6,5)
multiplying = calc.multiply(6,5)
dividing = calc.divide(6,5)

print(f'Summation is: {adding}')
print(f'Deducting is: {deducting}')
print(f'Multiplying is: {multiplying}')
print(f'Dividing is: {dividing}')