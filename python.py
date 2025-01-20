a = 2 

def some_function(num):
    global a
    a = a + num
    return a

print(a)
print(some_function(5))
print(a)
print(some_function(5))
print(a)
