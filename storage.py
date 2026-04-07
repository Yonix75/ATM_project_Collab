import json




# def load_data():
#     with open("account.json","r")as file:
#      my_bank = json.load(file)#Lit un fichier contenant du JSON et le convertit en objet Python.
#      return my_bank
#def save_data(bank):
   # with open("account.json","w")as file:
       # file =bank
        #json.dumps(file)# Convertit un objet Python en une chaîne de caractères (string) au format JSON.
    


def save_data(bank):
    data = {
        "accounts": [account.to_dict() for account in bank.accounts],
        "next_id": bank.nextCount_id
    }

    with open("account.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    from models import Bank, Account

    with open("account.json", "r") as file:
        data = json.load(file)

    accounts = [Account.from_dict(acc) for acc in data["accounts"]]

    bank = Bank(accounts, "000")
    bank.nextCount_id = data["next_id"]

    return bank