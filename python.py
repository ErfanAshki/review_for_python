class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def fullname(self):
        return f"{self.first_name}  {self.last_name}"
    
    
class Student(Person):
    pass


ali = Student('ali', 'alavi')
print(ali.fullname())
