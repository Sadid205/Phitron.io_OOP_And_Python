class Shop():
    Product_list = {}
    def __init__(self,name="Phitron") -> None:
        self.name = name
        self.Customer_list = {} # It is a Object of user Objects key is customer_id
        self.Seller_list = {} # It is a Object of Seller Objects here key is seller_id
         # It is a Object of Products here key is product_id
        
    def Sign_up(self,User_object): #User Object
         if User_object.who.lower() == 'customer':
            for _,value in self.Customer_list.items():
                if value.email == User_object.email:
                    print("You have already an account please login\n")
                    return
            self.Customer_list[User_object.user_id] = User_object
            print(f"{User_object.name} is a new customer in {self.name}\n")
         elif User_object.who.lower()=='seller':
            for _,value in self.Seller_list.items():
                if value.email == User_object.email:
                    print(f"You have already an account in this shop please login.Your email id is : {value.email}\n")
                    return
            self.Seller_list[User_object.user_id] = User_object
            print(f"{User_object.name} is a new seller in {self.name}\n")
    def Login(self,email,password,who):
        if who.lower() == 'customer':
            for _,value in self.Customer_list.items():
                if value.email == email and value.password==password:
                    print(f"Welcome to {self.name} shop {value.name}\n")
                    return value
            print("Invalid email or password !\n")
            return None
        elif who.lower()== 'seller':
            for _,value in self.Seller_list.items():
                if value.email==email and value.password==password:
                    print(f"Welcome to {self.name} Shop {value.name}")
                    return value
            print("Invalid email or password !\n")
            return None


    def Show_seller_list(self):
        if not self.Seller_list:
            print("Seller List is Empty: \n")
        else:
            for id,value in self.Seller_list.items():
                print(f"Here is the {self.name} shop's Seller List: \n")
                print(f"Seller Id:{id}\nSeller Name:{value.name}\nSeller Address:{value.address}\nSeller Email:{value.email}\nWho:{value.who}\n\n")
                print("<----------------------------------------------------------------------------------------------------------------------------------->")
                
            
    def Show_customer_list(self):
        if not self.Customer_list:
            print("Customer List is Empty")
        else:
            for id,value in self.Customer_list.items():
                print(f"Here is the {self.name} shop's Customer List: \n")
                print(f"Customer Id:{id}\nCustomer Name:{value.name}\nCustomer Address:{value.address}\nCustomer Email:{value.email}\nWho:{value.who}\n\n")
                print("<----------------------------------------------------------------------------------------------------------------------------------->")
      