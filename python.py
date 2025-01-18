import random

print('gol ya poch game')

cups = int(input('How many cups do you want ? ' ))
chances = int(input('How many chances you want to have ? ' ))

LINE_LENGTH = 10 

print()
print('-'*LINE_LENGTH)

ai_goal = random.randint(1,cups)
word = 's'


for _ in range(chances):
    if chances - _ == 1:
        word = ''
    
    print(f"{chances - _} chance{word} left")
    user_goal = int(input(f'select from {[1,cups]} : '))
    print()
    
    
    if user_goal == ai_goal :
        print('Right answer , congratulation')
        break
    else:
        print('Wrong answer')
        
    print()
    print('-'*LINE_LENGTH)
    
if user_goal == ai_goal :
    print('You win , thanks for your time')    
else:
    print(f'You lost because the right answer is {ai_goal}')
    print('Try again ? :)')
