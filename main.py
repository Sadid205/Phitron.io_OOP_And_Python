from bank import Bank
from user import User
from admin import Admin
import random

Phitron = Bank(100000,"Phitron")
while True:
        print("1 For create an account. ")
        print("2 For log in an account. ")
        print("3 For exit.")
        choose = int(input("Please enter a number: "))
        if  choose==1:
            while True:
                print("1 For create an admin account. ")
                print("2 For create a user account. ")
                print("3 For exit.")
                press = int(input("Please enter a number : "))
                if press==1:
                    admin_name = input("Please enter your name : ")
                    admin_email = input("Please enter your email address : ")
                    admin_password = input("Please enter your password : ")
                    admin_address = input("Please enter your address : ")
                    admin_role = input("Please enter your role (Example: admin) : ")
                    admin_id = random.randint(10**3,10**4-1)
                    if admin_role.lower()!='admin':
                        print("\nPlease write the correct spelling (Example: admin)\n")
                    else:
                        new_admin = Admin(name=admin_name,email=admin_email,password=admin_password,address=admin_address,role=admin_role,user_id=admin_id)
                        Phitron.Sign_Up(new_admin)        
                elif press==2:
                    user_name = input("Please enter your name : ")
                    user_email = input("Please enter your email address : ")
                    user_password = input("Please enter your password : ")
                    user_address = input("Please enter your address : ")
                    user_account_type = input("Please enter your account type (Saving or Current) : ")
                    user_role = input("Please enter your role (Example: user) : ")
                    user_id = random.randint(10**3,10**4-1)
                    if user_role.lower()!='user':
                        print("\nPlease write the correct spelling (Example: user)\n")
                    else:
                        new_user = User(name=user_name,email=user_email,address=user_address,account_type=user_account_type,password=user_password,role=user_role,user_id=user_id)
                        Phitron.Sign_Up(new_user)
                elif press==3:
                    break
                else:
                    print("Please enter correct number 1 or 2 or 3")         
        elif choose==2:
            while True:
                print("1 For admin login")
                print("2 For user login")
                print("3 For exit")
                press = int(input("Please enter a number : "))
                if press==1:
                    admin_role = input("Please enter your role (Example: admin) : ")
                    admin_user_id = int(input("Please enter your user id : "))
                    admin_password = input("Please enter your password : ")
                    if admin_role!='admin':
                        print("\nPlease write the correct spelling (Example: admin)\n")
                        break
                    admin = Phitron.Login(role=admin_role,user_id=admin_user_id,password=admin_password,bank=Phitron)
                    while True:
                        if admin!=None:
                            print("1 For delete user account ")
                            print("2 For see all user account ")
                            print("3 For see total balance ")
                            print("4 For total loan amount ")
                            print("5 For stop loan feature ")
                            print("6 For enable loan feature ")
                            print("7 For create an user account ")
                            print("8 For exit ")
                            press = int(input("Please Enter a number : "))
                            if press==1:
                                del_user_id = int(input("Please enter user id : "))
                                admin.Delete_user_account(Phitron,del_user_id)
                            elif press==2:
                                admin.See_all_user_account(Phitron)
                            elif press==3:
                                admin.See_total_balance(Phitron)
                            elif press==4:
                                admin.See_total_loan_amount(Phitron)
                            elif press==5:
                                admin.Stop_loan_feature(Phitron)
                            elif press==6:
                                admin.Enable_loan_feature(Phitron)
                            elif press==7:
                                ad_user_name = input("Please enter user name : ")
                                ad_user_email = input("Please enter user email address : ")
                                ad_user_password = input("Please enter user password : ")
                                ad_user_address = input("Please enter user address : ")
                                ad_user_account_type = input("Please enter user account type (Saving or Current) : ")
                                ad_user_role = input("Please enter user role (Example: user) : ")
                                ad_user_id = random.randint(10**3,10**4-1)
                                if ad_user_role!='user':
                                    print("\nPlease write the correct spelling (Example: user)\n")
                                else:
                                    ad_user = User(name=ad_user_name,email=ad_user_email,address=ad_user_address,account_type=ad_user_account_type,password=ad_user_password,role=ad_user_role,user_id=ad_user_id)
                                    admin.Create_an_user_account(ad_user,Phitron)    
                            elif press==8:
                                break
                            else:
                                print("Please enter a valid number from 1 to 6")
                        else:
                            print(f"This account does not exist on {Phitron.Bank_name} bank.\n")
                            break
                elif press==2:
                    user_role = input("Please enter your role : ")
                    user_user_id = int(input("Please enter your user id : "))
                    user_password = input("Please enter your password : ")
                    if user_role!='user':
                        print("\nPlease write the correct spelling (Example: user)\n")
                        break
                    user = Phitron.Login(role=user_role,user_id=user_user_id,password=user_password,bank=Phitron)
                    while True:
                        if user!=None:
                            print("1 For deposit balance")
                            print("2 For withdraw balance")
                            print("3 For check balance")
                            print("4 For check transaction history")
                            print("5 For take loan")
                            print("6 For transfer balance")
                            print("7 For exit")
                            select = int(input("Please select a number : "))
                            if select==1:
                                amount = int(input("Please enter amount : "))
                                user.Deposit_balance(Phitron,amount)
                            elif select==2:
                                self_amount = int(input("Please enter amount : "))
                                user.Withdraw_balance(Phitron,self_amount)
                            elif select==3:
                                user.Available_balance()
                            elif select==4:
                                user.Transaction_history_check()                           
                            elif select==5:
                                selfs_amount = int(input("Please enter amount : "))
                                user.Take_loan(Phitron,selfs_amount)                           
                            elif select==6:
                                ss_account_number = int(input("Please enter account number : "))
                                ss_amount = int(input("Please enter amount : "))
                                ss_transaction_id = random.randint(10**9,10**10-1)
                                user.Transfer_balance(ss_account_number,Phitron,ss_amount,ss_transaction_id)                       
                            elif select==7:
                                break
                            else:
                                print("Invalid input ! Please enter number from 1 to 7\n")
                        else:
                            print(f"This account does not exist on {Phitron.Bank_name} bank.\n")
                            break
                elif press==3:
                    break
                else:
                    print("Invalid input ! Please enter number from 1 to 3.\n")
        elif choose==3:
            break
        else:
            print("Invalid input ! Please enter number from 1 to 3\n")
    

    
    