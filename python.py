class Circle:
    pi=3.14
    
    def __init__ (self, r):
        self.r = r
        
    def calc_diameter(self):
        return f"diameter : {self.r * 2}"
        
    def calc_circumference(self):
        return f"circumference : {2 * Circle.pi * self.r}"
    
    def calc_area(self):
        return f"calc_area : {Circle.pi * self.r * self.r}"
    
    
c1 = Circle(10)
c2 = Circle(8)

print(c1.calc_diameter())
print(c1.calc_circumference())
print(c1.calc_area())
print()
print(c2.calc_diameter())
print(c2.calc_circumference())
print(c2.calc_area())
print()
