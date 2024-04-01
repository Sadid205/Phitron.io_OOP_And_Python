# 1. Convert string to Float
# number1 = input()
# number2 = input()
# float(number1)
# float(number2)

# sum = number1 + number2
# print(sum)

# 2.take 3 numbers from the user and give me the largest number as output
""" first = input()
second = input()
third = input()
fit = int(first)
sit = int(second)
tit = int(third)


if fit > sit and fit > tit:
    print('First value is greater: ',fit)
elif sit>fit and sit>tit :
    print('Second value is greater: ',sit)
else:
    print('Third value is greater: ',third)
 """

# 3.take 3 numbers from the user and give me the sum of the numbers

""" first_value = input()
second_value = input()
third_value = input()
ft = int(first_value)
st =  int(second_value)
tt = int(third_value)

sum = ft+st+tt
print(sum) """

# 4.run a loop and show me the odd numbers between 39 to 68

""" for i in range(39,68):
    if(i%2==1):
        print(i) """

number = int(input('Please insert your number: '))
if number <=100 and number >=80:
    print('Congratulation your grade is: A+ ')
elif number <80 and number >=70:
    print('Congratulation your grade is: A ')
elif number < 70 and number >=60:
    print('Congratulation your grade is: A-')
elif number < 60 and number >=50:
    print('Congratulation your grade is: B ')
elif number < 50 and number >=40:
    print('Congratulation your grade is: C ')
elif number < 40 and number >=33:
    print('Congratulation your grade is: D ')
else:
    print('Your are Fail !!')