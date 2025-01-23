def custom(num_list):
    copy_of_num_list = num_list.copy()
    
    copy_of_num_list.append(100)
    return copy_of_num_list
    
numbers = [1,2,3]

print(numbers)
print(custom(numbers))
print(numbers)

