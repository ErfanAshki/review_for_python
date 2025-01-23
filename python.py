def custom(num_list):
    num_list.append(100)
    return num_list
    
numbers = [1,2,3]

print(numbers)
custom(numbers)
print(numbers)

