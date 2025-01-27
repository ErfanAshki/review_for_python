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
    

john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 500)    
    
print(john_dep + david_dep)

john_dep += david_dep

print(john_dep)
print(david_dep)
