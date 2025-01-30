f = open('hi.txt', 'r')

names = f.read()
names = names.split('\n')

print(names)

while True:
    user_name = input('Enter your name : ')
    if user_name == 'exit':
        break
    names.append(user_name)
    
    print(names)
    
