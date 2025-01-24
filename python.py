def make_space (number_of_star , num) : 
    number_of_space = int((num - number_of_star) / 2) 
    print(number_of_space * ' ' , end= '') 
    print(number_of_star * '*' , end= '') 
    print(number_of_space * ' ')  





def make_diamond (num) :
    print()  
    for i in range(1,num+1,2) :
        make_space(i,num)   
    
    for i in range(1,num,2) :
        make_space(num-i-1 , num)    

    # for i in range (num) :
    #     if i < num / 2 : 
    #         print(i * 2 + 1) 
    #     else : 
    #         print((num - i) * 2 - 1 )  
      
user_number = int(input("Enter a number : ")) 

if user_number == 0 : 
    print('Invalid input , please enter a correct number')
elif user_number % 2 == 0 : 
    user_number += 1 


make_diamond(user_number) 
