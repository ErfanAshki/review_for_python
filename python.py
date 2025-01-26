class Shape:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
        
    def area(self):
        raise NotImplementedError("All shapes should be have own area method")
    

class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length
        
    def area(self):
        return self.side_length * self.side_length
        

class Circle(Shape):
    pi = 3.14

    def __init__(self, kind, name, r):
        super().__init__(kind, name)
        self.r = r

    def area(self):
        return Circle.pi * self.r * self.r
    
        
sq = Square('square', 'first_sq', 10)
ci = Circle('circle', 'first_ci', 10)

print(sq.area())
print(ci.area())

