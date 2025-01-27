class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        
    def __str__(self):
        return f"square with {self.side_length} length ."
    
    def __len__(self):
        return self.side_length
    
    def __del__(self):
        print (f"object with {self.side_length} length was deleted .")
    
    
s1 = Square(10)
s2 = Square(5)


print(s2)