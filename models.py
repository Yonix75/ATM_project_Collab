from datetime import *

class Bank:
    def __init__(self):
        pass
    
    
class Account:
    def __init__(self,pin,name,passwrd,money):
        self.pin=pin
        self.name=name
        self.money=money
        self.passwrd = str(passwrd)
        self.is_activated = True
        self.transaction = [ ]
        
        
        
        
    def auth(self,pin):
        if self.pin == pin:
           self.is_activated = True
           return self.pin
        else:
            print("is Incorrect")
            
    def addTransaction():
        pass
        
        
        
                
            
            
            
            
     
     
     
    
     