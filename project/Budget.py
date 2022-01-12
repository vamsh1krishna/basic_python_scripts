class category():

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
        if self.get_balance() > a:
            return True
        else:
            return False

    def deposit(self,a,b=None):
        self.dep={}
        self.dep['amount'] = float(a)
        self.dep['description'] = b
        self.ledger.append(self.dep)
        #print(self.ledger[0:])
        return self.ledger


    def withdraw(self,a,b=None):
        if self.check_funds(a) is True:
            self.wit = {}
            self.wit['amount'] = float(-a)
            self.wit['description']= b
            #print(self.wit)
            self.ledger.append(self.wit)
            #print(self.ledger)
            return self.ledger
        else:
            return False
    
    def transfer(self,amount,other):
        if self.get_balance() > amount:
            self.withdraw(amount,"Transfer to "+str(other.name))
            x=str(self.name)
            other.deposit(amount,"Transfer from "+x)
            return True
        else:
            return False

    def prnt(self):
        txt = self.name
        print(txt.center(30,"*"))
        for i in range(len(self.ledger)):
            x=self.ledger[i]['description']
            if x==None:
                x="None"
            x=x[:23]
            y=str(round(self.ledger[i]['amount'],2))[:7]
            print(x,y.rjust(30-len(x)))
        print("Total: ", self.get_balance())

def create_spend_chart(p,q,r):
    a=p.ledger[0]['amount']-p.get_balance()
    b=q.ledger[0]['amount']-q.get_balance()
    c=r.ledger[0]['amount']-r.get_balance()
    y = a+b+c
    def per_cent(x):
        return round((x/y*100)/10)*10
    ap = per_cent(a)
    bp = per_cent(b)
    cp = per_cent(c)

    def chart(ap,bp,cp):
        print("Percent spent by Category")
        for i in range(11):
            x=100-10*i

            def greater(a):
                if x<=a:
                    return "o"
                else:
                    return " "


            if i==0:
                print(x,"|"," ",greater(ap)," ",greater(bp)," ",greater(cp))
            elif i==10:
                print(" ",x,"|"," ",greater(ap)," ",greater(bp)," ",greater(cp))
            else:
                print("",x,"|"," ",greater(ap)," ",greater(bp)," ",greater(cp))
        print("    ","-"*14)
        for i in range(max(len(p.name),len(q.name),len(r.name))):
            def name(a,b):
                if len(a.name)>b:
                    return a.name[b]
                else:
                    return " "

            print("       ",name(p,i)," ",name(q,i)," ",name(r,i))
    chart(ap,bp,cp)


    

    
food = category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = category("Clothing")
food.transfer(50,clothing)
clothing.withdraw(25.55)
print(clothing.ledger)
auto = category("Auto")
auto.deposit(1000, "Intial deposit")
auto.withdraw(15)

food.prnt()
clothing.prnt()
auto.prnt()


create_spend_chart(food,clothing,auto)









