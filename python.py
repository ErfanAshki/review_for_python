class NegativeAgeError(Exception):
    pass


def check_age(age):
    if age < 0 :
        raise NegativeAgeError('Age can not be negative .')
    
    return f"Your age is {age}"


user_age = int(input('Enter your age : '))

print(check_age(user_age))
    
