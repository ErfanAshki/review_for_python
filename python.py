nums = [1,2,3,4]

def power_two(num):
    return num ** 2

def plus_ten(num):
    return num + 10


print(list(map(power_two,nums)))
print(list(map(plus_ten,nums)))
