import random


choices = ['s', 'p', 'r']
ai_choice = random.choice(choices) 
user_choice = input('select from rock , paper , scissor (r, p, s) : ')

if user_choice in choices :
    print(f'user_choice is {user_choice} and ai_choice is {ai_choice}')

    if user_choice == ai_choice:
        print('draw')

    elif (user_choice == 's' and ai_choice == 'p') or (user_choice == 'p' and ai_choice == 'r') or (user_choice == 'r' and ai_choice == 's'):
        print('you win')
        
    else:
        print('lost')
else:
    print('invalid input')
    
        