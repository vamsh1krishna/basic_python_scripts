class Category():

    def __init__(self,name):
        self.name = name
        self.ledger=[]
    
    def get_balance(self):
        x = 0
        #print(len(self.ledger))
        for i in range(len(self.ledger)):
            x = x + self.ledger[i]['amount']
            #print(x)
        return float(x)

    def check_funds(self,a):
        if self.get_balance() >= a:
            return True
        else:
            return False

    def deposit(self,a,b=None):
        self.dep={}
        self.dep['amount'] = float(a)
        if b==None:
            self.dep['description']=""
        else:
            self.dep['description']= b
        self.ledger.append(self.dep)
        #print(self.ledger[0:])
        


    def withdraw(self,a,b=None):
        if self.check_funds(a) is True:
            self.wit = {}
            self.wit['amount'] = float(-a)
            if b==None:
                self.wit['description']=""
            else:
                self.wit['description']= b
            #print(self.wit)
            self.ledger.append(self.wit)
            #print(self.ledger)
            return True
        else:
            return False
    
    def transfer(self,amount,other):
        if self.check_funds(amount) is True: 
            self.withdraw(amount,f"Transfer to {other.name}")
            other.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False


    def __str__(self):
        txt = self.name
        op = txt.center(30,"*")+"\n"
        """for item in self.ledger:
            op += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        op += f"Total: {format(self.get_balance(), '.2f')}"
        return op"""
    
        for i in range(len(self.ledger)):
            x=self.ledger[i]['description']
            if x==None:
                x=""
            op = op+f"{self.ledger[i]['description'][:23].ljust(23)}{format(self.ledger[i]['amount'], '.2f').rjust(7)}\n"
        op= op+ f"Total: {format(self.get_balance(), '.2f')}"
        return op


def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

    

  return(graph)
    




    

    
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50,clothing)
clothing.withdraw(25.55)
#print(clothing.ledger)
auto = Category("Auto")
auto.deposit(1000, "Intial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)


print(create_spend_chart([food,clothing,auto]))











