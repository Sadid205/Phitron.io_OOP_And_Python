class Shop:
    cart=[] # cart is a class attribute
    def __init__(self,buyer):
        self.buyer = buyer
    
    def add_to_cart(self,item):
        self.cart.append(item)

mehzbeeen = Shop('Meh Jabeeeen')
mehzbeeen.add_to_cart('shoes')
mehzbeeen.add_to_cart('Phone')
print(mehzbeeen.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
print(nisho.cart)