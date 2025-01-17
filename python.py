print('Welcome to this app')

number_of_numbers = int(input('How many numbers do want to enter ?'))

numbers_list = list()

for _ in range(number_of_numbers):
    user_number = int(input('Enter a number for Avg : '))
    numbers_list.append(user_number)
    
print(sum(numbers_list) / len(numbers_list))
