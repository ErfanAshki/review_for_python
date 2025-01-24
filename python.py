def divisors(num):
    divisors_list = []
    
    for i in range(1,num):
        if num % i == 0:
            divisors_list.append(i)
    
    return divisors_list

print(divisors(10))
print(divisors(12))
print(divisors(81))


def is_perfect(num):
    divisors_list = divisors(num)
    
    if sum(divisors_list) == num:
        return True
    return False

print(is_perfect(496))
print(is_perfect(8128))
print(is_perfect(81))
