class Deposit:
    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        
    def __str__(self):
        return f"Owner : {self.name} | amount : {self.amount}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name} , amount={self.amount})"
    

john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 500)    
    
print(repr(john_dep))
