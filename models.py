from datetime import *


class Bank:
    def init(self):
        pass


class Account:
    def __init__(self,id,name,pin,balance):
        
        self.id = id
        self.name=name
        self.balance=balance
        self.pin = pin
        self.is_activated = True
        self.transaction = [  ]
        

    def auth(self):
        id_client = (input("Enter your account ID: "))   # קבלת מזהה מהמשתמש
        pin_client = (input("enter your PIN: "))       # קבלת סיסמא מהמשתמש

        if id_client == self.id and pin_client == self.pin:
            self.is_activated = True
            self.id = id_client

            
            print("correct")
            return self.is_activated

        else:
            print("is Incorrect")
            self.is_activated = False
            
            
    def balance(self):
        print(self.balance) 
               
            
    

 

    def balance(user_balance):
     print(f"Your Balance now is {user_balance}")


acount1 =Account("123","niv", "123", 500, False, [])
acount2 =Account("123","yoni", "123", 1000, False, [])


acount1.auth()



def addTransaction():
    pass