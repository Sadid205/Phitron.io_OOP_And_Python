class Transaction:
    def __init__(self,sender_user_id,receiver_user_id,amount,transaction_id) -> None:
        self.Transaction_id = transaction_id
        self.Sender_user_id = sender_user_id
        self.Receiver_user_id = receiver_user_id
        self.Amount = amount