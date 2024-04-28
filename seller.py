from user import User
class Seller(User):
    def __init__(self, name, email, address, password, who, user_id) -> None:
        super().__init__(name, email, address, password, who, user_id)
        self.my_products = {} 

    def Add_product(self,product,shop): # product er object
        for _,value in shop.Product_list.items():
            if value.product_id == product.product_id:
                value.quantity +=product.quantity
                print(f"This {value.product_name} product is already added in this shop\n")
                return
        shop.Product_list[product.product_id] = product
        self.my_products[product.product_id] = product
        print(f"This {product.product_name} product is successfully added in this shop\n")
    def Remove_product(self,product_id,shop):
        for key,_ in shop.Product_list.items():
            if product_id==key:
                print(f"{shop.Product_list[key].product_name} product is deleted !\n")
                del shop.Product_list[key]
                del self.my_products[key]
                return
        print(f"This {product_id} id's product is not available in this shop\n")
    
    def View_my_product(self):
        if not self.my_products:
            print("Your products list is empty !")
        else:
            for key,value in self.my_products.items():
                print(f"Product Name:{value.product_name}\nProduct Price:{value.price}\nProduct Quantity:{value.quantity}\nProduct Id:{key}\n\n")
                print("<----------------------------------------------------------------------------------------------------------------------------------->")
    
                