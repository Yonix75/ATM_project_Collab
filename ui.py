import tkinter as tk
from models import *




class ATMApp():
    def __init__(self,root,Bank):
        self.root = root
        self.Bank = Bank
        self.current_account= None
        
    # פונקציות יו אי 
    
    def clear_screen(self):#she is destroy all of widgets in window (Buton , label , text)
      for widget in self.root.winfo_children():
        widget.destroy()
    
    # פונקציה כללית לקבלת אנטרי 
    def get_entery_filed(self, entery):
        try:
            return int(entery.get())
        except ValueError:
            print("Please enter a valid number")
            return None
        
    # פונקציה לקבלת האנטריז של מזהה וססימא והתחברות
    def get_enterys_valu(self):
        try:
           id_valu = int(self.entry_ID.get()) # קבלת המידע מהחלונית משתמש וסיסמא
           pin_valu = self.entry_PIN.get()
        except ValueError:
            new_window = tk.Toplevel(root)  # מייצר חלון חדש
            new_window.title("ERORR")
            new_window.geometry("250x150")  
            self.label = tk.Label(new_window, text="Please enter a valid numbers",font=("Arial", 10, "bold"),bd=0,highlightthickness=0)
            self.label.pack(pady=50)
            #self.title_label.config(text="Please enter a valid number")
            return None
        
        self.current_account=Bank.auth(my_bank,id_valu,pin_valu)
           
        if self.current_account:
                print( f"id: {id_valu} pin: {pin_valu}")    
                self.show_menu_screen()   
        else:
             self.title_label.config(text="Worng ID or PIN")
        
    def admin_login(self):
        try:
            admin_pin = (self.entry_pin.get())
        except ValueError:
            self.entery_label.config(text="Please enter a valid number")
            return None
        
        if admin_pin == my_bank.pinBoss:
            self.show_admin_menu_screen()
        else:
            self.entery_label.config(text="worng PIN")
            
        
    # פונקציות לקוח 
    
    def get_deposit(self):
        try:
            amount = int(self.entry_amount.get())
        except ValueError:
            self.label_amount.config(text="Please enter a valid number")
            return None
        
        result = self.current_account.deposit(amount)
        self.label_amount.config(text=result)
        
            
    
    def get_withdraw(self):
        try:
            amount = int(self.entry_amount.get())
        except ValueError:
            self.label_amount.config(text="Please enter a valid number")
            return None
        
        result = self.current_account.withdraw(amount)
        self.label_amount.config(text=result)
        
        
    def operationComplet(self):
        self.clear_screen()
        self.title_label = tk.Label(self.root,text="Operation Complet", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=50)#vertical title
        self.label_account = tk.Label(self.root, text="")
        self.back_button = tk.Button(self.root, text="Back", width=15,command=self.show_menu_screen)
        self.back_button.pack(pady=20)
   
    def get_Transaction(self):
      try:
        target = int(self.entry_ID.get())
        amount = float(self.entry_amount.get())
      except ValueError:
        self.label_amount.config(text="Please enter a valid number")
        self.label_target.config(text="Please enter a valid id")
        return None

      result = self.current_account.transfereTo(target, amount)
      self.label_account.config(text=result)
      #self.operationComplet()
    
    def get_Balance(self):
      self.show_balance_screen()
      balance = self.current_account.balanceaccount()
      self.label_account.config(text=balance)
      
      
    # פונקציות מנהל 
      
    # יצירת משתמש
    def get_create_acccount(self):
        try:
            name = (self.entry_nameacc.get())
            pin =  (self.entry_pinacc.get())
        except ValueError:
            self.done_label.config(text="Invalid input, Please try again")
            return None
        
        txt = my_bank.creatAccount(name, pin)
        self.done_label.config(text=txt)
        
        
      
      
    # פונקציות הצגת חלונות 

    def show_login_screen(self):
        self.clear_screen()
        
        # logo plus petit
        logo_image = tk.PhotoImage(file="2.png")
        logo_small = logo_image.subsample(4, 4)

        logo_label = tk.Label(main_frame, image=logo_small, bd=0, bg="white", highlightthickness=0)
        logo_label.place(x=-85, y=-90)   # plus à gauche
        logo_label.image = logo_small
        
        self.title_label = tk.Label(self.root,text="Welcome", font=("Helvetica", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=40)#vertical title

        #=======================================================entry your number id
        self.label_account = tk.Label(self.root, text="ID",bd=0,highlightthickness=0)
        self.label_account.pack()
        self.entry_ID = tk.Entry(self.root, width=25)#entry input
        #ATMApp.get_entery_valu
        self.entry_ID.pack(pady=10)

        #=======================================================entry your number pin
        self.label_account = tk.Label(self.root, text="PIN Number")
        self.label_account.pack()
        self.entry_PIN = tk.Entry(self.root, width=25,show="*")#entry input 
        self.entry_PIN.pack(pady=5)


        self.login_button = tk.Button(self.root, text="Login", width=15, command=self.get_enterys_valu)
        self.login_button.pack(pady=15)

        self.admin_button = tk.Button(self.root, text="Admin", width=15, command=self.show_admin_login_screen)
        self.admin_button.pack()
        
        
        
    
    def show_menu_screen(self):
        self.clear_screen()
        balance = self.current_account.balanceaccount()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0, fg="#FF0000")#title center window
        self.title_label.place(x=270, y=40)#vertical title
        
        # שלום לשם המשתמש
        self.username_label = tk.Label(self.root,text=f"Hello {self.current_account.name}", font=("Arial", 13, "bold"),bd=0,highlightthickness=0)
        self.username_label.place(x=70, y=50)
        
        # הצגת המאזן
        self.blanace_label = tk.Label(self.root,text=f"Balance: {balance}", font=("Arial", 13, "bold"),bd=0,highlightthickness=0)
        self.blanace_label.place(x=560, y=50)
        
        #  כפתור הפקדה
        self.deposit_button = tk.Button(self.root, text="Deposit", width=15,command=self.show_deposit_screen)
        self.deposit_button.place(x=40, y=150)
        
        # כפתור משיכה 
        self.withdraw_button = tk.Button(self.root, text="Withdraw", width=15,command=self.show_withdraw_screen)
        self.withdraw_button.place(x=40, y=250)
        
        # כפתור הצג עובר ושב
        self.balance_button = tk.Button(self.root, text="Balance", width=15,command=self.get_Balance)
        self.balance_button.place(x=560, y=150)
       
        # כפתור העברה
        self.transfer_button = tk.Button(self.root, text="Transfer", width=15,command=self.show_Transfer_screen)
        self.transfer_button.place(x=560, y=250)
        
        # כפתור יציאה 
        self.back_button = tk.Button(self.root, text="Log out", width=15,command=self.show_login_screen)
        self.back_button.place(x=300, y=400)

    def show_admin_login_screen(self):
        self.clear_screen()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=15)#vertical title
        
        self.login_label = tk.Label(self.root,text="Admin Login", font=("Arial", 13, "bold"),bd=0,highlightthickness=0)
        self.login_label.pack(pady=40)
        
        self.entery_label = tk.Label(self.root,text="Enter your PIN", font=("Arial", 10, "bold"),bd=0,highlightthickness=0)
        self.entery_label.pack(pady=15)
        
        self.entry_pin = tk.Entry(self.root, width=25)#entry input
        #ATMApp.get_entery_valu
        self.entry_pin.pack(pady=10)
        
        # כפתור אנטר
        self.enter_button = tk.Button(self.root, text="Login", width=15, command=self.admin_login)
        self.enter_button.pack(pady=10)
        
        # כפתור יציאה 
        self.back_button = tk.Button(self.root, text="back", width=15,command=self.show_login_screen)
        self.back_button.place(x=300, y=400)
        
    def show_admin_menu_screen(self):
        self.clear_screen()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0, fg="#FF0000")#title center window
        self.title_label.place(x=270, y=40)
        
        #   כפתור יצירת חשבון
        self.creat_account_button = tk.Button(self.root, text="Create new account", width=15,command=self.show_account_creation_screen)
        self.creat_account_button.place(x=40, y=150)
        
        # כפתור הצגת כל החשבונות 
        self.show_accounts_button = tk.Button(self.root, text="All my accounts", width=15)
        self.show_accounts_button.place(x=40, y=250)
        
        # כפתור הצג חסימה שחרור 
        self.block_account_button = tk.Button(self.root, text="Block / Release", width=15)
        self.block_account_button.place(x=560, y=150)
       
    
        
        
        # כפתור יציאה 
        self.back_button = tk.Button(self.root, text="Log out", width=15,command=self.show_login_screen)
        self.back_button.place(x=300, y=400)

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

    def show_withdraw_screen(self):
        self.clear_screen()
        
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=50)#vertical title
        
        self.label_amount = tk.Label(self.root, text="Enter the amount you would like to withdraw",bd=0,highlightthickness=0,)
        self.label_amount.pack(pady=30)
        
        self.entry_amount = tk.Entry(self.root, width=25)#entry input
        self.entry_amount.pack(pady=5)
        self.enter_button = tk.Button(self.root, text="Enter", width=15,command=self.get_withdraw)
        self.enter_button.pack(pady=10)
        self.back_button = tk.Button(self.root, text="Back", width=15,command=self.show_menu_screen)
        self.back_button.pack(pady=20)

    def show_balance_screen(self):
        self.clear_screen()
         
        self.label_account = tk.Label(self.root, text="")
        self.label_account.pack()
        self.title_label = tk.Label(self.root,text="SOLD", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=50)#vertical title
        self.label_account = tk.Label(self.root, text="")
        self.label_account.pack()
        self.back_button = tk.Button(self.root, text="Back", width=15,command=self.show_menu_screen)
        self.back_button.pack(pady=20)
    
    
    def show_Transfer_screen(self):
        self.clear_screen()
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.pack(pady=50)#vertical title
        self.label_target = tk.Label(self.root, text="Targted account ID",bd=0,highlightthickness=0)
        self.label_target.pack()
        self.entry_ID = tk.Entry(self.root, width=25)#entry input
        #ATMApp.get_entery_valu
        self.entry_ID.pack(pady=5)

        #=======================================================entry your number pin
        self.label_account = tk.Label(self.root, text="Amount")
        self.label_account.pack()
        self.entry_amount = tk.Entry(self.root, width=25)#entry input 
        self.entry_amount.pack(pady=5)


        self.login_button = tk.Button(self.root, text="Enter", width=15, command=self.get_Transaction)
        self.login_button.pack(pady=10)
        self.back_button = tk.Button(self.root, text="Back", width=15,command=self.show_menu_screen)
        self.back_button.pack(pady=20)
        
     
    def show_account_creation_screen(self):
        self.clear_screen()
        self.title_label = tk.Label(self.root,text="ATM Machine", font=("Arial", 20, "bold"),bd=0,highlightthickness=0)#title center window
        self.title_label.place(x=270, y=40)
        
        # לייבל שם 
        self.name_label = tk.Label(self.root,text="Enter you name: ", font=("Arial", 13, ),bd=0,highlightthickness=0)
        self.name_label.place(x=150, y=150)
        
        # אנטרי של שם
        self.entry_nameacc = tk.Entry(self.root, width=25)#entry input
        self.entry_nameacc.place(x=130, y=190)
        
        # לייבל של סיסמא
        self.pin_label = tk.Label(self.root,text="Enter your PIN", font=("Arial", 13, ),bd=0,highlightthickness=0)
        self.pin_label.place(x=450, y=150)
        
        # אנטרי של סיסמא
        self.entry_pinacc = tk.Entry(self.root, width=25)#entry input
        self.entry_pinacc.place(x=430, y=190)
        
        # כפתור אנטר
        self.enter_button = tk.Button(self.root, text="Creat Account!", width=15, command=self.get_create_acccount)
        self.enter_button.place(x=300, y=270)
        
        # לייבל אישור ביצוע 
        self.done_label = tk.Label(self.root, font=("Arial", 13, ),bd=0,highlightthickness=0)
        self.done_label.place(x=250, y=320)
        
        
        
        # כפתור חזרה
        self.back_button = tk.Button(self.root, text="Back", width=15,command=self.show_admin_menu_screen)
        self.back_button.place(x=300, y=400)
        
        
#creat windows


import tkinter as tk

root = tk.Tk()
root.title("MAZE BANK")
root.geometry("720x480")
root.iconbitmap("mazeBank.ico")

# contour rouge seulement autour
border_frame = tk.Frame(root, bg="red")
border_frame.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = tk.Frame(border_frame, bg="white")
main_frame.place(x=2, y=2, relwidth=1, relheight=1, width=-4, height=-4)

app = ATMApp(main_frame, Bank=None)
app.show_login_screen()


# =================================================cursor
# cursor_image = tk.PhotoImage(file="cursor_transparent_32.png")
# cursor_label = tk.Label(main_frame, image=cursor_image, bd=0, bg="white", highlightthickness=0)
# cursor_label.place(x=0, y=0)
# cursor_label.image = cursor_image
# root.config(cursor="none")
# def move_fake_cursor(event):
#     x = event.x_root - root.winfo_rootx()
#     y = event.y_root - root.winfo_rooty()

#     cursor_label.place(x=x, y=y)
#     cursor_label.lift()

# root.bind_all("<Motion>", move_fake_cursor)

# def move_fake_cursor(event):
#     cursor_label.place(x=event.x, y=event.y)

# main_frame.bind("<Motion>", move_fake_cursor)
root.mainloop()