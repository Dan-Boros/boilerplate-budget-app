class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):

        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([log.amount for log in self.ledger])
    
    def transfer(self, amount, toOther: Category):

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {toOther.name}")
            toOther.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __repr__(self):
        # *************Food*************
        # initial deposit        1000.00
        # groceries               -10.15
        # restaurant and more foo -15.89
        # Transfer to Clothing    -50.00
        # Total: 923.96
        title = '{:*^30}'.format(self.name)
        
        total = f'Total: {self.get_balance()}'
        
        itemsTemplate = "{0: <23}{1:7.2f}"
        items = [total.format(item['description'], item['amount']) for item in self.ledger]
        
        lines = [title, *items, total]

        return "\n".join(lines)


def create_spend_chart(categories):
    pass