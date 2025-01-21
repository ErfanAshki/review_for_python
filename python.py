import random 

list_of_word = ['hi', 'bye', 'sun', 'sky', 'moon', 'fire', 'water'] 


def start_game():
    print('Welcome to this game')
    print('Hope you win')
    print()
    print('-' * 15)


def get_input():
    
    while True:
        user_choice = input("Enter your guess : ") 

        if user_choice.isalpha():
            return user_choice
        else:
            print('Your guess is wrong please enter a correct guess .')


def valid_input():
    while True:
        user_input = get_input()
        
        if user_input in list_of_word:
            return user_input
        else:
            print('Invalid input')
        

def run_game(rounds):
    start_game()
    ai_input = random.choice(list_of_word)
    print(f"number of guess you have : {rounds}")
    
    for i in range(rounds):
        user_input = valid_input()
        
        if user_input == ai_input:
            print('Right answer , Well done')
            return
        else:
            print('Wrong answer')
            print(f"number of guess you have : {rounds -1 -i}")
        print('-' * 15)
    
    print('You lost')
    print(f"The right guess is {ai_input} .")
    

run_game(3)

