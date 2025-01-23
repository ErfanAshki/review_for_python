numbers = [1,2,3,4,5,6,7]

def plus_one_even_numbers(num):
  
    if num % 2 == 0:
        return num + 1
    else:
        return num


def plus_two_odd_numbers(num):

    if num % 2 == 1:
        return num + 2 
    else:
        return num
    
    

print(list(map(plus_one_even_numbers, numbers)))
print(list(map(plus_two_odd_numbers, numbers)))
