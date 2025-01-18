import random

print('Welcome to paper scissor rock game')

# num_of_rounds = int(input('how many round do you want to play ? '))
choices = ['p', 's', 'r']

user_point = 0
ai_point = 0 


while True:
    ai_choice = random.choice(choices)
    user_choice = input('Select from paper scissor rock (p, s, r) : ')
    print()

    if user_choice in choices:
        # num_of_rounds -= 1
        
        if user_choice == ai_choice:
            print(f"your choice is {user_choice} and ai choice is {ai_choice}")
            print('draw')
        elif (user_choice == 'p' and ai_choice == 'r') or (user_choice == 's' and ai_choice == 'p') or (user_choice == 'r' and ai_choice == 's'):
            print(f"your choice is {user_choice} and ai choice is {ai_choice}")
            print('user +1')
            user_point += 1 
        else:
            print(f"your choice is {user_choice} and ai choice is {ai_choice}")
            print('ai + 1')
            ai_point += 1
    else:
        print('Invalid input , please select from (p, s, r)')
    
    
    print(f"user point = {user_point}  --  ai point = {ai_point}")
    print()
    print('------------------')
    
    if user_choice == 5 : 
        print('You win the game')
        break
    elif ai_point == 5:
        print('You lost , want try again ? :)') 
        break      

print("Have a good day")


# if user_point > ai_point : 
#     print('You win the game')
# elif user_point == ai_point :
#     print('Same points!!!')
# else:
#     print('You lost , want try again ? :)')
    
