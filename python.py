names = ['lale ahmadi','mmd naseri','john johnson']

def get_first_name(name):
    return name.split(' ')[0]

def get_last_name(name):
    return name.split(' ')[1]

print(list(map(get_first_name,names)))
print(list(map(get_last_name,names)))
