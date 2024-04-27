class Admin:
    def __init__(self,name,email,password,address,role,user_id) -> None:
        self.Name = name
        self.Email = email
        self.Password = password
        self.Address = address
        self.Role = role
        self.User_id = user_id

    def Delete_user_account(self,bank,user_id):
        for id,_ in bank.User_list.items():
            if user_id == id:
                del bank.User_list[user_id]
                print(f"THIS {id} ACCOUNT IS SUCCESSFULLY DELETED.\n")
                return 
        print(f"THIS {user_id} ACCOUNT DOES NOT EXIST IN {bank.Bank_name} BANK.\n")
    def See_all_user_account(self,bank):
        if not bank.User_list:
            print("USER LIST IS EMPTY.\n")
        else:
            for id,value in bank.User_list.items():
                print(f"NAME:{value.Name}\nEMAIL ADDRESS:{value.Email}\nACCOUNT NUMBER:{value.Account_number}\nID:{id}\n")
                print("<------------------------->")
        
    def See_total_balance(self,bank):
        print(f"{bank.Total_amount} TAKA.\n")
    def See_total_loan_amount(self,bank):
        print(f"{bank.Total_loan_amount} TAKA.\n")
    def Stop_loan_feature(self,bank):
        bank.Is_bankrupt = True
        print("SUCCESSFULLY STOPPED BANK LOAN FEATURE.\n")
    def Enable_loan_feature(self,bank):
        bank.Is_bankrupt = False
        print("SUCCESSFULLY ENABLED BANK LOAN FEATURE.\n")
    def Create_an_user_account(self,user,bank):
        for _,value in bank.User_list.items():
            if user.Email == value.Email:
                print(f"YOU HAVE ALREADY AN ACCOUNT IN THIS BANK.HERE IS YOUR ACCOUNT NUMBER : {value.Account_number} AND USER ID : {value.User_id} .PLEASE LOGIN.\n")
                return
        bank.User_list[user.User_id]=user
        print(f"YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT.HERE IS YOUR ACCOUNT NUMBER : {user.Account_number} AND USER ID : {user.User_id}.\n")
