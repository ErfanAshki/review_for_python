def max_min_sum_len(*args, list_of_numbers):
    list_of_numbers.append(args)
    
    return max(args) , min(args) , sum(args) , len(args)


list_of_numbers = []

print(max_min_sum_len(1,2,3,5,8,5,88,2,663, list_of_numbers=list_of_numbers))
print(list_of_numbers)
