numbers = [10,2,14,52,3,-4,0,27]

def more_than_10(num):
    if num > 10 :
        return True
    return False
    
print(list(filter(more_than_10, numbers)))

