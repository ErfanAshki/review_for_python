class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def fullname(self):
        return f"{self.first_name}  {self.last_name}"
    
    
class Student(Person):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major
        
    def fullname(self):
        return f"{self.first_name}  {self.last_name}  {self.major}"


ali = Student('ali', 'alavi', 'computer Engineering')
print(ali.fullname())
