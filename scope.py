balance = 3000

def by_things(item,price):
    # local scope variable
    # you can access global variable with using without using the global keyword
    
    dream_phone = 'Xphone'
    # if you want to modify a global variable, you have to use the global keyword
    global balance
    print(f'previous balance value {balance}')
    balance = balance - price 
    print(f'balance after buying {item}',balance)

# print (dream_phone)
by_things('sunglass',1000)
print('global balance after buy',balance)