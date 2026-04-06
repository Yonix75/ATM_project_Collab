from datetime import *

class Account:
    def __init__(self,id,name,pin,balance,): 
        
        self.id = int(id)
        self.name=name
        self.balance=balance
        self.pin = pin
        self.is_activated = True
        self.transactions = [  ]
        
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
    
    def transfereTo():
        
        user_account = my_bank.auth()
        if user_account:
            myName = user_account.name
            myId= user_account.id
            target_account_id = int(input("Enter the ID of the account you would like to transfer to: ").strip())
            amount = int(input("Enter the amount you would like to tranfer: ").strip())
            target_account=None
            
            for i in my_bank.accounts:
               if i.id == target_account_id:
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

            if amount > user_account.balance:
              print("Insufficient funds")
              return
           
                    #target_account = i 
                    #targetname=i.name
                   # targetid=i.id
        else:
            return print("account dont exist")            
            
                
        
        
        user_account.balance -= amount
        target_account.balance += amount

        user_account.newTransaction(f"Transfer sent to ID: {targetid} name: {targetname} ", amount) #! אולי כדי להכניס מי העביר 
        target_account.newTransaction(f"Transfer received to ID:{myId} name: {myName}", amount) #! כנל להכניס מי שלח את הכסף

        print(f"Transferred {amount} to account {target_account.name}")
        print(f"Your new balance: {user_account.balance}")
            
        
         
        
            
    def deposit():
        user_account = my_bank.auth()
        
        if user_account:
            amount = int(input("How much money you would like to deposit: ").strip())
            if amount < 0:
                print("You cannot tpye negative numbers")
                exit()
            else:
                user_account.balance+=amount
                print(f"new Balance in your Account is {user_account.balance}")
                user_account.newTransaction("deposite",amount)
               
    def withdraw():
        user_account = my_bank.auth()
        
        if user_account:
            if user_account.is_activated:
                amount = float(input("Please type the amount you would like to withdraw: ").strip())
                if amount > user_account.balance:
                    print("You are poor")
                else: 
                    user_account.balance -= amount
                    print(f"your new balance is {user_account.balance}")
                    user_account.newTransaction("withdraw",amount)
            else:
                print("Wrong PIN, goodbye")
                exit() 
                      
    def balanceaccount(self):
        print(self.balance)
        
         
         
class Bank():
    def __init__(self, accounts, pinBoss):
        self.accounts = accounts
        self.pinBoss = pinBoss
        self.nextCount_id = 1001 
        
    # def login(self):
    #     self.auth()    
        
    def auth(self):
        user_id = int(input("Enter your account ID: ").strip())
        pin = (input("Enter your PIN: ").strip())
        
        for account in self.accounts:
            if user_id == account.id and pin == account.pin:
                print(f"Welcome {account.name}")
                
                return account
            
        print("worng ID or PIN")
    
            
              
        
    def creatAccount(self):
        name = input("What your name: ")
        pin = input("Choose your PIN: ")
        for i in my_bank.accounts:
            self.nextCount_id=i.id
        
        self.nextCount_id+=1            
        Account_id = self.nextCount_id
        self.is_activated = True
        self.nextCount_id +=1
        new_Account = Account(Account_id, name, pin, 0 )
        self.accounts.append(new_Account)
        print("Account created successfully!")
    
    
    
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
        for account in self.accounts:
            print(account)
            
        


    
acount1 =Account(1001,"niv", "123", 500)
acount2 =Account(1002,"yoni", "123", 41500)
acount3 =Account(1003,"dan", "123", 34500)
# acount4 =Account(1004,"ron", "123", 4500)

#my_bank = Bank([acount1,acount2,acount3],123)
my_bank = Bank([acount1,acount2,acount3],123)



#my_bank.creatAccount()
#my_bank.creatAccount()
#my_bank.show_all_accounts()
#Account.deposit()
#Account.withdraw()
#Account.transfereTo()
#my_bank.account_finder()
#Account.deposit()
# my_bank.accounts[0].deposit()