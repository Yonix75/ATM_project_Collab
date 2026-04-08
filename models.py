from datetime import *
from storage import *

class Account:
    def __init__(self,id,name,pin,balance): 
        
        self.id = int(id)
        self.name=name
        self.balance=balance
        self.pin = pin
        self.is_activated = True
        self.transactions = [  ]
    
    def to_dict(self):
      return {
        "id": self.id,
        "name": self.name,
        "pin": self.pin,
        "balance": self.balance,
        "is_activated": self.is_activated,
        "transactions": self.transactions
    }
      
    @classmethod
    def from_dict(cls, data):
     account = cls(
        data["id"],
        data["name"],
        data["pin"],
        data["balance"]
    )
     account.is_activated = data["is_activated"]
     account.transactions = data["transactions"]
     return account 
      
        
    def __str__(self):
        return (f"Account ID: {self.id} User name: {self.name}, Balance: {self.balance}, Pin: {self.pin}, Account active: {self.is_activated}, Transaction history: {self.transactions}")

    def is_pin_correct(self):
        id_client = int((input("Enter your account ID: ").strip()))  # קבלת מזהה מהמשתמש
        pin_client = (input("enter your PIN: ").strip())       # קבלת סיסמא מהמשתמש

        if id_client == self.id and pin_client == self.pin:
            self.is_activated = True
           
            print("correct")
            return self.is_activated

        else:
            print("is Incorrect")
            self.is_activated = False
            
    
            
    def newTransaction(self,transaction_type,amount):
      newTransaction = {
          "type": transaction_type,
          "amount": float(amount),
          "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      }
      self.transactions.append(newTransaction)         
            
    
    
    def show_Transaction(self):
        print(self.transactions)
    
    
    
    
    
                
    
    def transfereTo(self,target,amount):
        
        #user_account = my_bank.auth()
        if self.is_activated:
            #myName = user_account.name
            #myId= user_account.id
            #target_account_id = int(input("Enter the ID of the account you would like to transfer to: ").strip())
            #amount = int(input("Enter the amount you would like to tranfer: ").strip())
            target_account=None
            
            for i in my_bank.accounts:
               if i.id == target:
                  target_account = i
                  targetname=i.name
                  targetid=i.id
                  break

            if target_account is None:
             print("Targeted account not found")
             return

            if not target_account.is_activated:
             print("Target account is blocked")
             return

            if amount <= 0:
             print("Invalid amount")
             return

            if amount > self.balance:
              print("Insufficient funds")
              return
           
                    #target_account = i 
                    #targetname=i.name
                   # targetid=i.id
        else:
            return print("account dont exist")            
            
                
        
        
        self.balance -= amount
        target_account.balance += amount

        self.newTransaction(f"Transfer sent to ID: {target_account.id} name: {target_account.name} ", f"{amount}") 
        target_account.newTransaction(f"Transfer received to ID:{self.id} name: {self.name}", amount) 
        save_data(my_bank)#saveeeee
        print(f"Transferred {amount} to account {target_account.name}")
        print(f"Your new balance: {self.balance}")
        return f"Transfer sent to: {target_account.name} \n ID number: {target_account.id} \n {amount}$ has been sent"
            
        
         
        
            
    def deposit(self,amount):
        
        #self.is_activated
        
        if self.is_activated:
            #amount = int(input("How much money you would like to deposit: ").strip())
            if amount < 0:
                #self.label_amount.config(text="You cannot tpye negative numbers")
                print("You cannot tpye negative numbers")
                return f"You cannot tpye negative numbers"
                
            else:
                self.balance+=amount
                print(f"The money has been deposited ! The new Balance in your Account is: {self.balance}$")
                self.newTransaction("deposite",amount)
                save_data(my_bank)
                return f"The money has been deposited ! \n The new Balance in your Account is: {self.balance}$"
               
    def withdraw(self,amount):
        #user_account = my_bank.auth()
        
        
            if self.is_activated:
                #amount = float(input("Please type the amount you would like to withdraw: ").strip())
                if amount > self.balance:
                    print("You are poor")
                    #self.label_amount.config(text="you do not have the funds")
                    return f"you do not have the funds"
                elif amount < 0:
                    #self.label_amount.config(text="You cannot tpye negative numbers")
                    print("You cannot tpye negative numbers")
                    return f"You cannot tpye negative numbers"
                else: 
                    self.balance -= amount
                    
                    print(f"your new balance is {self.balance}")
                    
                    self.newTransaction("withdraw",amount)
                    save_data(my_bank)
                    return f"The money has been deposited ! \n The new Balance in your Account is: {self.balance}₪"
            else:
                print("Wrong PIN, goodbye")
                exit() 
                      
    def balanceaccount(self):
        print(self.balance)
        return f"{self.balance}$"
        
         
         
class Bank():
    def __init__(self, accounts, pinBoss):
        self.accounts = accounts
        self.pinBoss = pinBoss
        self.nextCount_id = 1000 
        
    def is_open(self):
       
        return self.is_activated
        
    def auth(self,user_id,pin):
       # user_id = int(input("Enter your account ID: ").strip())
        #pin = (input("Enter your PIN: ").strip())
        
        for account in self.accounts:
            if user_id == account.id and pin == account.pin:
                if user_id!=1000:
                  print(f"Welcome {account.name}")
                  self.is_activated = True
                  return account
                else:
                  print(f"Welcome {account.name}") 
                  return my_bank.directorLogin()
                     
            
        print("worng ID or PIN")
    
            
              
        
    def creatAccount(self, name, pin):
        # name = input("What your name: ")
        # pin = input("Choose your PIN: ")
        for i in my_bank.accounts:
            self.nextCount_id=i.id
        
        self.nextCount_id+=1            
        Account_id = self.nextCount_id
        self.is_activated = True
    
        new_Account = Account(Account_id, name, pin, 0 )
        self.accounts.append(new_Account)
        save_data(self)#save new account
        print("Account created successfully!")
        return "Account created successfully!"
    
    
    
    def account_finder(self):
        id_to_finde = int(input("Enter the ID of the account you want to finde: ").strip())
        account_found = None
        
        for account in self.accounts:
            if account.id == id_to_finde:
                print("Account found!: ")
                account_found = account
                print(account_found)
                return account_found
            
        print("account not found")
        
    
    def show_all_accounts(self):
        load=load_data()
        for account in load.accounts:
          print(account)
            
    def show_All_Transaction(self):
        
        
        for account in self.accounts:
         print(f"Account ID: {account.id} | Name: {account.name}")
        
        if not account.transactions:
            print("  No transactions found")
        else:
            for transaction in account.transactions:
                print(f"  Type: {transaction['type']}")
                print(f"  Amount: {transaction['amount']}")
                print(f"  Date: {transaction['date']}")
                print("  --------")
            
    
    def directorLogin(self):
        self.show_all_accounts()
        
        
          
           
try:
    my_bank = load_data()
except FileNotFoundError:
    my_bank = Bank([], "000")      
    



if __name__ == "main":
    
    my_bank.show_all_accounts()
    Account.withdraw()
    my_bank.show_all_accounts()
    Account.transfereTo()
