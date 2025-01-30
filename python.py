names = []

with open('hi.txt', 'r') as f : 
    for name in f.read().split('\n'):
        names.append(name) 
        
print(names)
        
