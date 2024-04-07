class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        product = {'Item':item,"Price":price,"Quantity":quantity}
        self.cart.append(product)
    # homework
    def remove_item(self,item):
        for items in self.cart:
            if items['Item']==item:
                self.cart.remove(items)
                print(f'Your Removed Item is :{items}')

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total+=item['Price']*item['Quantity']
        print('Total Price',total)
        if amount < total:
            print(f'Please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')
    
swapan = Shopping('Alan Swapon')
swapan.add_to_cart('alu',50,6)
swapan.add_to_cart('dim',12,24)
swapan.add_to_cart('rice',50,5)
print(swapan.cart)
swapan.checkout(600)
swapan.checkout(1600)


print(swapan.cart)
swapan.remove_item('alu')
print(swapan.cart)