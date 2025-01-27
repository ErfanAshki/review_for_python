class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        
    def __str__(self):
        return f"square with {self.side_length} length ."
    
    def __len__(self):
        return self.side_length
    
    
s1 = Square(10)
s2 = Square(5)

print(s1)
print(s2)
print()
print(len(s1))
print(len(s2))
