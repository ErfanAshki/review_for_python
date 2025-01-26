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


class Teacher(Person):
    def __init__(self, first_name, last_name, university, department):
        super().__init__(first_name, last_name)
        self.university = university
        self.department = department
        
    def fullname(self):
        return f"{self.first_name}  {self.last_name}  {self.university} {self.department}"


majid_teac = Teacher('majid', 'jasemi', 'tehran', 'math')
print(majid_teac.fullname())


ali_stu = Student('ali', 'alavi', 'computer Engineering')
print(ali_stu.fullname())


help(Teacher)
