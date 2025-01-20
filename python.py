def is_even(num):
    if num % 2 == 0:
        return True

def is_odd(num):
    if num % 2 == 1:
        return True    
    
def separate_even_odd_numbers(list):
    even_nums = []
    odd_nums = []
    
    for num in list:
        if is_even(num):
            even_nums.append(num)
        elif is_odd(num):
            odd_nums.append(num)
            
    return even_nums , odd_nums


numbers_list = [1,5,3,4,6,52,69,63,65,96,30]

print(separate_even_odd_numbers(numbers_list))
