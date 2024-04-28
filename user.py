from abc import ABC
from shop import Shop
class User(ABC):
    def __init__(self,name,email,address,password,who,user_id) -> None:
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.who = who
   
    

    