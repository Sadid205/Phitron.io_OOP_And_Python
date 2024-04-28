from user import User


class Customer(User):
    def __init__(self, name, email, address, password, who, user_id) -> None:
        super().__init__(name, email, address, password, who, user_id)
        self.cart = {} # it is a objects of product objects and it has a key which is product_id
    def Add_to_cart(self,product_id,shop):
        for id,value in self.cart.items():
            if id==product_id:
                self.cart[id].quantity+=1
                print(f"Your {value.product_name} product is already exist on the cart and here is the quantity: {self.cart[id].quantity}\n")
                return

        for id,value in shop.Product_list.items():
            if id== product_id:
                self.cart[id] = value
                self.cart[id].quantity = 1
                print(f"Your{value.product_name} product is added on cart!\n")
                return
        print("This product is not available in this shop!\n")

    def Remove_from_cart(self,product_id):
        for id,value in self.cart.items():
            if id == product_id:
                print(f"{value.product_name} is deleted from your cart.\n")
                del self.cart[id]        
                return
        print("This product is not available in this shop !\n")
    
    def Buy_product(self,product_name,total_amount,product_quantity,product_id):
        for _,value in self.cart.items():
            if value.product_id==product_id :
                total_price = product_quantity*value.price
                if value.quantity < product_quantity:
                    print(f"The only {value.quantity} Items available\n")
                    return False
                else:
                    if total_amount >= total_price:
                        print(f"Here is your product: {value.product_name} and your extra money is {total_amount-total_price}\n")
                        return True
                    else:
                        print(f"Please add {total_price-total_amount} money extra !\n")
                        return False
        print(f"This {product_name} product can not found your cart.Here is the product id:{product_id}.Please add this item in your cart.")

    def View_products(self,shop):
        if not shop.Product_list:
            print("No Products Available")
        else:
            for id,value in shop.Product_list.items():
                print(f"Product Name:{value.product_name}\nProduct Id:{id}\nProduct Quantity:{value.quantity}\nProduct Price:{value.price}\n\n")
                print("<----------------------------------------------------------------------------------------------------------------------------------->")

    def View_my_cart(self):
        if not self.cart:
            print("Your cart is empty,Please add some products on your cart.\n")
        else:
            for id,value in self.cart.items():
                print(f"Product Name:{value.product_name}\nProduct Id:{id}\nProduct Quantity:{value.quantity}\nProduct Price:{value.price}\n\n")
                print("<----------------------------------------------------------------------------------------------------------------------------------->")
