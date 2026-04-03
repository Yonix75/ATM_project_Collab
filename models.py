from datetime import *


class Bank:
    def init(self):
        pass


class Account:
    def init(self, id, name ,pin ,balance, is_activated, transaction ):
        self.id = id
        self.name=name
        self.balance=balance
        self.pin = pin
        self.is_activated = is_activated
        self.transaction = transaction

    def auth(self):
        id_client = (input("Enter your account ID: "))   # קבלת מזהה מהמשתמש
        pin_client = (input("enter your PIN: "))       # קבלת סיסמא מהמשתמש

        if id_client == self.id and pin_client == self.pin:
            self.is_activated = True
            print("correct")
            return self.id

        else:
            print("is Incorrect")
            self.is_activated = False



acount1 =Account("123","niv", "123", 500, False, [])




def addTransaction():
    pass