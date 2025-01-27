class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return f"Line : a=({self.a[0]},{self.a[1]})  b=({self.b[0]},{self.b[1]})"
        
        
    def calc_length(self):
        return ((self.b[1] - self.a[1]) ** 2 + (self.b[0] - self.a[0]) ** 2) ** 0.5
    
    
    def calc_slope(self):
        return (self.b[1] - self.a[1]) / (self.b[0] - self.a[0])
    
    
line1 = Line((1,1) , (3,3))

print(line1)
print(line1.calc_length())
print(line1.calc_slope())

line2 = Line((4,9) , (8,1))

print(line2)
print(line2.calc_length())
print(line2.calc_slope())

