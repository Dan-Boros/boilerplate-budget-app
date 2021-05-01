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
        return sum([item["amount"] for item in self.ledger])

    def get_spendings(self):
        return sum([item["amount"] for item in self.ledger if item["amount"] < 0])
    
    def transfer(self, amount, toOther):

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
        items = [itemsTemplate.format(item['description'][:23], item['amount']) for item in self.ledger]
        
        lines = [title, *items, total]

        return "\n".join(lines)


def create_spend_chart(categories):
    title = "Percentage spent by category"

    catSpendings = {cat.name: cat.get_spendings() for cat in categories}
    total = sum([spending for _, spending in catSpendings.items()])
    catPercents = {name: spending * 100 / total for name, spending in catSpendings.items()}

    longestCategory = max([len(name) for name, _ in catSpendings.items()])
    noCats = len(categories)

    names = [list(f"{name: <{longestCategory}}") for name, _ in catSpendings.items()]
    namesTransponsed = list(map(list, zip(*names)))
    
    chartNames = [" " * 5 + "  ".join(line) + " " * 2 for line in namesTransponsed]

    chartGraph = []
    for perc in range(100, -1, -10):
        rawLine = [ "o" if catPercent >= perc else " " for name, catPercent in catPercents.items()] + [""]
        line = "{0: >3}| {1}".format(perc, "  ".join(rawLine)) 
        chartGraph.append(line)

    dashedLine = " " * 4 + "-" * (1 + 3 * noCats)
    finalLines = [title] + chartGraph + [dashedLine] + chartNames

    return "\n".join(finalLines)
