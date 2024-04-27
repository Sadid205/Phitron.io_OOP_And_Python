import random
from transaction import Transaction
class User:
    def __init__(self,name,email,address,account_type,password,role,user_id) -> None:
        self.Name = name
        self.Email = email
        self.Address = address
        self.Account_type = account_type
        self.Balance = 0
        self.Account_number = random.randint(10**14,10**15-1)
        self.Transaction_history = [] # It contains Transaction object 
        self.Take_loan_times = 0
        self.User_id = user_id
        self.Password = password
        self.Role = role
    def Deposit_balance(self,bank,amount):
        bank.Total_amount+=amount
        self.Balance+=amount
        for id,value in bank.User_list.items():
            if id==self.User_id:
                print(f"{value.Name}, YOU HAVE SUCCESSFULLY DEPOSIT {amount} TAKA\n")
                return
        print(f"YOUR ACCOUNT IS NOT EXIST IN {bank.Bank_name} BANK\n")
        return
    def Withdraw_balance(self,bank,amount):
        if self.Balance < amount:
            print(f"INSUFFICIENT BALANCE! YOU HAVE ONLY {self.Balance} TAKA LEFT IN YOUR ACCOUNT\n")
        else:
            if bank.Total_amount < amount:
                print(f"CURRENTLY,{bank.Bank_name} BANK DOES NOT HAVE {amount} TAKA IN VAULT.PLEASE WAIT SOME TIMES\n")
            else:
                for id,_ in bank.User_list.items():
                    if self.User_id == id:
                        bank.Total_amount-=amount
                        self.Balance-=amount
                        print(f"YOU HAVE SUCCESSFULLY WITHDRAW {amount} TAKA IN YOUR BALANCE FROM {bank.Bank_name} BANK.\n")
                        return
                print(f"{self.User_id} ID DOES NOT HAVE ANY ACCOUNT IN {bank.Bank_name} BANK\n")

    def Available_balance(self):
        print(f"YOUR BALANCE IS {self.Balance} TAKA\n")
    def Transaction_history_check(self):
        if not self.Transaction_history:
            print(f"YOUR TRANSACTION HISTORY IS EMPTY.PLEASE DO A TRANSACTION AFTER THAT CHECK IT.\n")
        else:
            for value in self.Transaction_history:
                print(f"SENDER USER ID:{value.Sender_user_id}\nRECEIVER USER ID:{value.Receiver_user_id}\nAMOUNT:{value.Amount}\nTRANSACTION ID:{value.Transaction_id}\n")
                print("<------------------------------------------------>")
    def Take_loan(self,bank,amount):
        if bank.Is_bankrupt==False:
            if bank.Total_amount > amount:
                if self.Take_loan_times>=2:
                    print(f"YOU CAN NOT TAKE LOAN MORE THAN TWICE.YOU HAVE ALREADY TAKEN LOAN {self.Take_loan_times} TIMES.\n")
                else:
                    for id,_ in bank.User_list.items():
                        if id==self.User_id:
                            self.Balance+=amount
                            bank.Total_amount-=amount
                            bank.Total_loan_amount+=amount
                            self.Take_loan_times+=1
                            print(f"YOU HAVE SUCCESSFULLY TAKE LOAN {amount} TAKA FROM {bank.Bank_name} BANK.\n")
                            return
                    print(f"THIS USER DOES NOT EXIST IN {bank.Bank_name} BANK.\n")
                    return 
            else:
                print(f"CURRENTLY,{bank.Bank_name} BANK DOES NOT HAVE {amount} TAKA IN VAULT.PLEASE WAIT SOME TIMES\n")
        else:
            print(f"THIS {bank.Bank_name} BANK DECLARED BANKRUPTCY.SO, YOU CAN'T TAKE LOAN.\n")
    def Transfer_balance(self,account_number,bank,amount,transaction_id):
        for _,value in bank.User_list.items():
            if value.Account_number == account_number:
                if self.Balance > amount:
                    for us_id,_ in bank.User_list.items():
                        if us_id == self.User_id:
                           self.Balance-=amount
                           value.Balance+=amount
                           new_transaction = Transaction(sender_user_id=self.User_id,receiver_user_id=value.User_id,amount=amount,transaction_id=transaction_id)
                           self.Transaction_history.append(new_transaction)
                           print(f"YOU HAVE SUCCESSFULLY TRANSFERRED {amount} TAKA TO {value.Account_number} ACCOUNT\n")
                           return 
                    print(f"YOUR ID: {self.User_id}.THIS ACCOUNT DOES NOT EXIST.\n")
                else:
                    print(f"THIS TIME ONLY {self.Balance} TAKA AVAILABLE IN YOUR ACCOUNT. YOU CAN'T TRANSFER {amount} TAKA TO {value.Account_number} ACCOUNT\n")
                    return
        print(f"THIS {account_number} ACCOUNT DOES NOT EXIST IN {bank.Bank_name} BANK\n")

   