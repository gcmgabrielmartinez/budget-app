class Category:
    def __init__(self, category: str):
      self.category = category
      self.ledger = []


    def deposit(self, amount: int, description = ""):
      self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount: int, description = ""):
      if self.check_funds(amount):
        self.ledger.append({"amount":-amount, "description": description})
        return True
      else:
        return False      


    def get_balance(self):
      balance = 0
      for cashflow in self.ledger:
        balance += cashflow.get("amount")
      return balance


    def transfer(self, amount, object_to):
      if self.check_funds(amount):
        self.ledger.append({"amount":-amount, "description": "Transfer to " + object_to.category})
        object_to.deposit(amount, "Transfer from " + self.category)
        return True
      else:
        return False


    def check_funds(self, amount):
      return self.get_balance() >= amount

    def __str__(self) -> str:
      extract = ""
      extract += self.category.center(30, "*") +"\n"
      for cashflow in self.ledger:
        extract += cashflow.get("description")[:23].ljust(23) + str(f"{cashflow.get('amount'):.2f}").rjust(7) + "\n"

      extract += "Total: " + f"{self.get_balance():.2f}"
      return extract


def create_spend_chart(categories):
    spents = {}

    for category in categories:
      spent = 0
      for cashflow in category.ledger:
        if cashflow.get("amount") < 0:
          spent += cashflow.get("amount")
      spents.update({category.category: spent})

    total_spent = sum([s for s in spents.values()])

    for cat in spents.keys():
      spents[cat] = int(spents[cat]/total_spent*10)*10
    #print(spents)

    #printing chart
    chart = "Percentage spent by category\n"
    for perc in range(100, -10, -10):
      chart += str(perc).rjust(3) + "| "
      for cat in spents.keys():
        if spents[cat] >= perc:
          chart += "o  "
        else:
          chart += "   "
      chart +="\n"
    chart += "    " + "---"*len(spents) + "-\n"

    greatest = sorted(spents.keys(), key = len, reverse = True)[0]

    for i in range(len(greatest)):
      chart += "    "
      for cat in spents.keys():
        try:
          chart += " "+ cat[i] + " "
        except:
          chart += "   "
      if i < len(greatest)-1:
        chart +=" \n"
      else:
        chart += " "

    return chart