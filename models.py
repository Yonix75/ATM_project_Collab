from datetime import *





class Bank:
    def __init__(self):
        pass
    
    
class Account:
    def __init__(self, id, name ,pin ,balance, is_activated, transaction ):
        self.id = id
        self.name=name
        self.balance=balance
        self.pin = str(pin)
        self.is_activated = False
        self.transaction = [ ]


        
acount1 =Account(123,"niv", 500, "123", False, [])



        
id_client = int(input("Enter your account id: "))
pin_client = int(input("enter your PIN: "))
    
def auth(self):
    
    id_client = int(input("Enter your account id"))   # קבלת מזהה מהמשתמש
    pin_client = int(input("enter your PIN: "))       # קבלת סיסמא מהמשתמש

    if id_client == self.id and pin_client == self.pin:
        self.is_activated = True
        print("correct")
        return self.id
        
    else:
        print("is Incorrect")
            
def addTransaction():
    pass
    


auth(acount1)

                
            
            
            
            
     
     
     
    
     