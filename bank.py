class Bank:
    def __init__(self,total_amount,bank_name) -> None:
        self.Bank_name = bank_name
        self.Total_amount = total_amount
        self.User_list = {} # It contains User Object and key is user Object's user_id and value is User Object.
        self.Admin_list = {} # It contains Admin Object and key is admin Object's user_id and value is Admin Object.
        self.Is_bankrupt = False
        self.Total_loan_amount = 0
    
    def Sign_Up(self,user):
        if user.Role.lower()=='user':
            for _,value in self.User_list.items():
                if value.Email == user.Email:
                    print(f"YOU HAVE ALREADY AN ACCOUNT WITH ACCOUNT NUMBER : {value.Account_number}.PLEASE LOG IN.\n")
                    return
            self.User_list[user.User_id] = user
            print(f"YOU HAVE SUCCESSFULLY SIGN UP INTO {self.Bank_name} BANK.YOUR ACCOUNT NUMBER IS {user.Account_number}.YOUR USER ID IS : {user.User_id}.NOW YOU ARE {user.Role.upper()}.\n")
        elif user.Role.lower()=='admin':
            for _,value in self.Admin_list.items():
                if value.Email == user.Email:
                    print(f"YOU HAVE ALREADY AN ACCOUNT WITH USER ID : {value.User_id}.PLEASE LOG IN.\n")
                    return
            self.Admin_list[user.User_id] = user
            print(f"YOU HAVE SUCCESSFULLY SIGN UP INTO {self.Bank_name} BANK.YOUR USER ID IS: {user.User_id}.NOW YOU ARE {user.Role.upper()}.\n")
        else:
            print("PLEASE ENTER CORRECT SPELLING OF 'admin' or 'user'.\n")        
    
        
    def Login(self,role,user_id,password,bank):
        if role=='user':
            for id,value in self.User_list.items():
                if id==user_id and password == value.Password:
                    print(f"WELCOME {value.Name}. YOU HAVE SUCCESSFULLY LOGGED IN INTO {bank.Bank_name} BANK AS {role.upper()}.YOUR USER ID IS : {user_id}.\n")
                    return value
            print(f"THIS {user_id} ID DOES NOT EXIST IN THIS BANK.PLEASE CREATE A NEW ACCOUNT.\n")
            return None
        elif role=='admin':
            for id,value in self.Admin_list.items():
                if id==user_id and password == value.Password:
                    print(f"WELCOME {value.Name}. YOU HAVE SUCCESSFULLY LOGGED IN INTO {bank.Bank_name} BANK AS {role.upper()}.YOUR USER ID IS : {user_id}.\n")
                    return value
            print(f"THIS {user_id} DOES NOT EXIST IN THIS BANK.PLEASE CREATE A NEW ACCOUNT.\n")
            return None
        else:
            print("PLEASE ENTER CORRECT SPELLING OF 'admin' or 'user'.\n")
        