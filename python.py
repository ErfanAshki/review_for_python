def divisors(num):
    divisors_list = []
    
    for i in range(1,num+1):
        if num % i == 0:
            divisors_list.append(i)
    
    return divisors_list

print(divisors(10))
print(divisors(12))
print(divisors(81))
