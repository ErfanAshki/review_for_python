def factorial(number):
    result = 1
    
    for num in range(1, number + 1):
        result *= num
    
    return result


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(10))
