def sum_number_of_list(list):
    result = 0

    for num in list:
        result += num
        
    return result

a = [1,2,3,10,-8,0,-5,21]

print(sum_number_of_list(a))
