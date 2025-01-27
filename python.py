class Contains:
    def __init__(self, items):
        self.items = items
        
    def __contains__(self, other):
        return other in self.items
    
    
a = Contains([1,2,3,4,5])

print(a.__contains__(7))
print(a.__contains__(3))
