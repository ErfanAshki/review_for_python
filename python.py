print('Welcome to this app')

number_of_numbers = int(input('How many numbers do want to enter ?'))

numbers_list = list()

while number_of_numbers > 0:
    user_number = int(input('Enter a number for Avg : '))
    numbers_list.append(user_number)
    number_of_numbers -= 1    
        
print(sum(numbers_list) / len(numbers_list))
