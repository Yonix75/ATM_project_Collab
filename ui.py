import tkinter as tk
from models import *



class ATMApp():
    def __init__(self,root,Bank):
        self.root = root
        self.Bank = Bank
        self.current_account= None
        
    def clear_screen(self):#she is destroy all of widgets in window (Buton , label , text)
      for widget in self.root.winfo_children():
        widget.destroy()
    
    def get_entery_filed(self, entery):
        try:
            return int(entery.get())
        except ValueError:
            print("Please enter a valid number")
            return None
        
    def get_enterys_valu(self):
           id_valu = int(self.entry_ID.get()) # קבלת המידע מהחלונית משתמש וסיסמא
           pin_valu = self.entry_PIN.get()
           self.current_account=Bank.auth(my_bank,id_valu,pin_valu)
           
           if self.current_account:
                print( f"id: {id_valu} pin: {pin_valu}")    
                self.show_menu_screen()    
        
    def get_deposit(self):
        try:
            amount = int(self.entry_amount.get())
        except ValueError:
            self.label_amount.config(text="Please enter a valid number")
            return None
        
        result = self.current_account.deposit(amount)
        self.label_amount.config(text=result)
        
            
    
    def get_withdraw(self):
        Account.withdraw()
   
    def get_Transaction(self):
       Account.transfereTo()
    
    def get_history(self):
        pass

    def show_login_screen(self):
        self.clear_screen()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=15)#vertical title

        #=======================================================entry your number id
        self.label_account = tk.Label(self.root, text="ID",bd=0,highlightthickness=0)
        self.label_account.pack()
        self.entry_ID = tk.Entry(self.root, width=25)#entry input
        #ATMApp.get_entery_valu
        self.entry_ID.pack(pady=5)

        #=======================================================entry your number pin
        self.label_account = tk.Label(self.root, text="PIN Number")
        self.label_account.pack()
        self.entry_PIN = tk.Entry(self.root, width=25,show="*")#entry input 
        self.entry_PIN.pack(pady=5)


        self.login_button = tk.Button(self.root, text="Login", width=15, command=self.get_enterys_valu)
        self.login_button.pack(pady=10)

        self.admin_button = tk.Button(self.root, text="Admin", width=15)
        self.admin_button.pack()
        
        
        
    
    def show_menu_screen(self):
        self.clear_screen()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=15)#vertical title
        
        #  כפתור הפקדה
        self.deposit_button = tk.Button(self.root, text="Deposit", width=15,command=self.show_deposit_screen)
        self.deposit_button.place(x=40, y=150)
        
        # כפתור משיכה 
        self.withdraw_button = tk.Button(self.root, text="Withdraw", width=15,command=self.get_withdraw)
        self.withdraw_button.place(x=40, y=250)
        
        # כפתור הצג עובר ושב
        self.balance_button = tk.Button(self.root, text="Balance", width=15,)
        self.balance_button.place(x=560, y=150)
       
        # כפתור העברה
        self.transfer_button = tk.Button(self.root, text="Transfer", width=15,command=self.get_Transaction)
        self.transfer_button.place(x=560, y=250)

    def show_deposit_screen(self):
        self.clear_screen()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=50)#vertical title
        
        self.label_amount = tk.Label(self.root, text="Enter the amount you would like to deposit",bd=0,highlightthickness=0,)
        self.label_amount.pack(pady=30)
        
        self.entry_amount = tk.Entry(self.root, width=25)#entry input
        self.entry_amount.pack(pady=5)
        self.enter_button = tk.Button(self.root, text="Enter", width=15,command=self.get_deposit)
        self.enter_button.pack(pady=10)
        self.back_button = tk.Button(self.root, text="Back", width=15,command=self.show_menu_screen)
        self.back_button.pack(pady=20)



#creat windows
root = tk.Tk()
#custom windows
root.title("ATM")
root.geometry("720x480")
#root.iconbitmap("pngwing.com.ico")
root.config(background='#4065A4')


app = ATMApp(root, Bank=None)
#app.show_menu_screen()
app.show_login_screen()


    

#display window
root.mainloop()
#my_bank.auth(entry_ID,entry_PIN)