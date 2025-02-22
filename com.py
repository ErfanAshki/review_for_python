import pickle

names = []

while True:
    name_input = input('Enter name : ')
    
    if name_input == 'exit':
        break
    
    names.append(name_input)
    
print(names)


with open('name.txt', 'wb') as f : 
    pickle.dump(names, f)
    
    