class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = list()
    
  #the deposit method 
  def deposit(self,amount,item =""):
    self.ledger.append({"amount": amount, "description":item})

  #withdraw method that handles transactions
  def withdraw(self,amount,item=""):
    
    if(self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description":item})
      return True
    return False
  #get balance method for the user to check their spending
  def get_balance(self):
    initialCash = 0
    for thing in self.ledger:
      initialCash += thing["amount"]
    return initialCash
  #transfer method
  def transfer(self,amount,budgetAcc):
    if(self.check_funds(amount)):
      self.withdraw(amount,"Transfer to " + budgetAcc.name)
      budgetAcc.deposit(amount, "Transfer from " + self.name)
      return True
    return False
    
  #to check if the spending equals or less to the money at hand
  def check_funds(self, amount):
    
    if(self.get_balance()>=amount):
      return True
    return False

  #formats the string display for the items and their costs
  def __str__(self):
    
    title = f"{self.name:*^30}\n"
    
    List_items = ""
    
    total = 0
    for item in self.ledger:
      List_items += f"{item['description'][0:23]:23}" + f"{item ['amount']:>7.2f}" +'\n'
      
      total+=item['amount']

    results = title + List_items + "Total: "+str(total)
    return results

  #helper for the spending chart
  def get_withdrawls(self):
    total =0
    for item in self.ledger:
      if item["amount"]<0:
        total += item["amount"]
    return total


 #creates the spending chart
def create_spend_chart(categories):

  results = "Percentage spent by category\n"
  i=100
  totals = getTotals(categories)
  while i >= 0:
    cat_spaces =" "
    for total in totals:
      if total * 100 >=i:
        cat_spaces +="o "
      else: 
        cat_spaces +="  "
    results +=str(i).rjust(3) + "|" + cat_spaces + ("\n")
    i -= 10

  dashes = "-" + "---"*len(categories)
  names = []
  x_axis = ""
  for cat in categories :
    names.append(cat.name)
  maxi = max(names,key=len)

  for x in range(len(maxi)):
    nameStr = '     '
    for name in names:
      if x >= len(name):
        nameStr += "   "
      else :
        nameStr += name[x] + "  "

    if (x != len(maxi) -1 ):
      nameStr += '\n'

    x_axis += nameStr
  
  results += dashes.rjust(len(dashes)+4) + "\n" + x_axis
  return results
  
  #helps the spending chart method by counting up the totals
def getTotals(categories):
  total=0
  breakdown = []
  for categ in categories:
    total += categ.get_withdrawls()
    breakdown.append(categ.get_withdrawls())
  rounded = list(map(lambda x: truncate(x/total), breakdown))
  return rounded 
  
  #helper for the spending chart
def truncate(n):
  multiplier = 10
  return int(n * multiplier) / multiplier

