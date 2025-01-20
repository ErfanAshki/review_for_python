def sum_numbers(*args):
    result = 0

    for num in args:
        result += num
    
    return result


print(sum_numbers(1,5,8,6,4,2,10,2,5,9,1))
