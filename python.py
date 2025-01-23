names = ['parrinaz khodash', 'erfan', 'mmd kivii', 'lale', 'ahmad']

def give_just_full_names(str):
    if len(str.split(' ')) > 1:
        return True
    return False
    
    
print(list(filter(give_just_full_names, names)))

