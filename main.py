from product import Product
from seller import Seller
from shop import Shop
from customer import Customer
import random

Phitron_shop = Shop()

while True:
    print("Press 1 for Sign Up As a Customer")
    print("Press 2 for Sign Up As a Seller")
    print("Press 3 for Login")
    print("Press 4 for Exit")
    choose = int(input("Enter Your Input : "))
    if choose == 1:
        user_name = input("Enter Your Name : ")
        user_email = input("Enter Your Email : ")
        user_address = input("Enter Your Address : ")
        user_password = input("Enter Your Password : ")
        user_who = input("Please Enter Who You Are (Example: Customer) : ")
        user_user_id = random.randint(10**3,10**4-1)
        new_customer=None
        if user_who.lower()!='customer':
            print("Please write the correct spelling of 'Who You Are Input' (Example: Customer)\n")
        else:
            new_customer = Customer(name=user_name,email=user_email,address=user_address,password=user_password,who=user_who,user_id=user_user_id)
            Phitron_shop.Sign_up(new_customer)
    elif choose == 2:
        seller_name = input("Enter Your Name : ")
        seller_email = input("Enter Your Email : ")
        seller_address = input("Enter Your Address : ")
        seller_password = input("Enter Your Password : ")
        seller_who = input("Please Enter Who You Are (Example: Seller) : ")
        seller_user_id = random.randint(10**3,10**4-1)
        new_seller=None
        if seller_who.lower()!='seller':
            print("Please write the correct spelling of 'Who You Are Input' (Example: Seller)\n")
        else:
            new_seller = Seller(name=seller_name,email=seller_email,address=seller_address,password=seller_password,who=seller_who,user_id=seller_user_id)
            Phitron_shop.Sign_up(new_seller)
    elif choose == 3:
        while True:
            print("\nPlease Login : \n")
            print("Press 1 for Customer")  
            print("Press 2 for Seller")
            print("Press 3 for exit")
            press = int(input("Please choose 1 to 3 : "))
            if press == 1:
                customer_email = input("Please Enter Your Email : ")
                customer_password = input("Please Enter Your Password : ")
                customer_who = input("Please Enter Who You Are (Example: Customer) : ")
                shops_customer=None
                if  customer_who.lower()!='customer':
                    print("Please write the correct spelling of 'Who You Are Input' (Example: Customer)\n")
                else:
                    shops_customer = Phitron_shop.Login(email=customer_email,password=customer_password,who=customer_who)
                if not Phitron_shop.Customer_list:
                    print("There Is No Customer In This Shop,Please Sign Up A Customer\n")
                    break
                while True:
                    if shops_customer!=None:
                        print("Press 1 for Products List")
                        print("Press 2 for Add To Cart")
                        print("Press 3 for Remove From Cart")
                        print("Press 4 for Buy Product")
                        print("Press 5 for View My Cart")
                        print("Press 6 for Exit")
                        cus_choose = int(input("Please Choose Any Number From 1 to 6 : "))
                        if cus_choose==1:
                            shops_customer.View_products(Phitron_shop)
                        elif cus_choose==2:
                            pr_id = int(input("Please Enter Product Id : "))
                            shops_customer.Add_to_cart(product_id=pr_id,shop=Phitron_shop)
                        elif cus_choose==3:
                            r_id = int(input("Please Enter Product Id : "))
                            shops_customer.Remove_from_cart(product_id=r_id)
                        elif cus_choose==4:
                            p_name = input("Please Enter Product Name : ")
                            p_id = int(input("Please Enter Product Id: "))
                            p_price = int(input("Please Enter Total Price : "))
                            is_success = shops_customer.Buy_product(product_name=p_name,total_amount=p_price,product_id=p_id)
                            if is_success !=None:
                                shops_customer.Remove_from_cart(product_id=p_id)
                                if is_success.quantity <= 0 :
                                    del Phitron_shop.Product_list[p_id]
                                    print(f"This {p_id} product is deleted.")
                        elif cus_choose==5:
                            shops_customer.View_my_cart()
                        elif cus_choose==6:
                            break
                        else:
                            print("Please Enter 1 to 6 Numbers\n")
                    else:
                        print("Your Account Is Not Available\n")
                        break
            elif press==2:
                s_email = input("Please Enter Your Email : ")
                s_password = input("Please Enter Your Password : ")
                s_who = input("Please Enter Who You Are (Example: Seller) : ")
                shops_seller=None
                if s_who.lower()!='seller':
                    print("Please write the correct spelling of 'Who You Are Input' (Example: Seller)\n")
                else:
                    shops_seller = Phitron_shop.Login(email=s_email,password=s_password,who=s_who)
                if not Phitron_shop.Seller_list:
                    print("There Is No Seller In This Shop,Please Sign Up A Seller.")
                    break
                while True:
                    if shops_seller != None:
                        print("\nPress 1 for Add Product")
                        print("Press 2 for Remove Product")
                        print("Press 3 for View My Product")
                        print("Press 4 for Seller List")
                        print("Press 5 for Customer List")
                        print("Press 6 for Exit\n")
                        ss_choose = int(input("Please Choose Any Number From 1 to 6 :"))
                        if ss_choose == 1:
                            sp_name = input("Please Enter Product Name : ")
                            sp_price = int(input("Please Enter Product Price : "))
                            sp_quantity = int(input("Please Enter Product Quantity : "))
                            sp_id = random.randint(10**3,10**4-1)
                            new_product = Product(product_name=sp_name,price=sp_price,quantity=sp_quantity,product_id=sp_id)
                            shops_seller.Add_product(new_product,Phitron_shop)
                        elif ss_choose == 2:
                            sp_id = int(input("Please Enter Your Product Id : "))
                            shops_seller.Remove_product(product_id=sp_id,shop=Phitron_shop)
                        elif ss_choose == 3:
                            shops_seller.View_my_product()
                        elif ss_choose==4:
                            Phitron_shop.Show_seller_list()
                        elif ss_choose==5:
                            Phitron_shop.Show_customer_list()
                        elif ss_choose == 6:
                            break
                    else:
                        print("Your Account Is Not Available\n")
                        break
            elif press==3:
                break
            else:
                print("Invalid Input ! Please Enter 1 to 3\n")
    elif choose==4:
        break
    else:
        print("Invalid Input Please Press 1 to 4\n")  
        