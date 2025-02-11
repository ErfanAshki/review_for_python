def something():
    def add_two_numbers(a, b):
        return a + b
    
    return add_two_numbers


a = something()
print(a(2,3))
print(a)
