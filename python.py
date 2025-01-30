f = open('hi.txt', 'r')

try:
    names = f.read()
    names = names.split('\n')
    print(names)
        
finally:
    f.close()
    
