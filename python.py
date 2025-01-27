class Deposit:
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        
    def __str__(self):
        return f"Owner : {self.name} | amount : {self.amount}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name} , amount={self.amount})"
    
    def __add__(self, other):
        name = self.name + '|' + other.name
        amount = self.amount + other.amount
        return Deposit(name , amount)
    
    def __iadd__(self, other):
        self.amount += other.amount
        other.amount = 0
        return self
    
    def __eq__(self, other):
        return self.amount == other.amount
    
    def transfer(self, other, amount):
        if self.amount < amount:
            print('Not enough amount for transfer')
            return
        
        self.amount -= amount
        other.amount += amount
        print(f"{amount} amount was transferred from {self.name} account to {other.name} account")
    
    
    def deposit(self, amount):
        if amount < 0:
            print('Amount could not be less than 0')
            return
        
        self.amount += amount
        

john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 500)    
    

john_dep.deposit(250)
david_dep.deposit(400)

print(john_dep)
print(david_dep)
