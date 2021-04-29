class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        deposit = {"amount": amount, "description": description}
        self.ledger.append(deposit)

    def withdraw(self, amount, description=""):
        isEnough = self.check_funds(amount)
        obj = {"amount": -amount, "description": description}
        self.ledger.append(obj)
        # ToDo: Check Ledger if enough in ledger
        return False

    def get_balance(self):
        return "balance of current Category"
    
    def transfer(self, amount, other):
        isEnough = self.check_funds(amount)
        return False

    def check_funds(self, amount):
        return False
    
    def __repr__(self):
        return ""


def create_spend_chart(categories):
    pass