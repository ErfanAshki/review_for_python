while True:
    user_number = input('Enter a number : ')

    try:
        result = int(user_number)
        break
    except ValueError :
        try:
            result = float(user_number)
            break
        except ValueError:
            print('You should enter a number .')


print(f"The number is {result}")    
