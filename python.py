print('determine prime number')


while True:
    prime = True

    user_number = int(input('Enter your number : '))
    
    for _ in range(2,user_number):
        if user_number % _ == 0:
            prime =False
            break
        
    if prime == True:
        print('number is prime')
    else:
        print(f'number is not prime because {user_number} % {_}')
        
    print()

