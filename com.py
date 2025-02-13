numbers = []

for nums in range(2,50):
    prime = True
    
    for i in range(2,nums):
        if nums % i == 0:
            prime = False
            break
     
    if prime:   
        numbers.append(nums)
    

print(numbers)

primes = [x for x in range(2,50) if all(x % y != 0 for y in range(2,x))]

print(primes)
