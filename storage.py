import json





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