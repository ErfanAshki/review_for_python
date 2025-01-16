# numbers = [1,5,4,54,25,10,22,11]

# for num in numbers:
#     if num % 2 == 0:
#         print(num, 'even')
#     elif num % 2 == 1:
#         print(num, 'odd')

my_str = 'I sending my resume to a lot companies'       

count_e = 0
count_m = 0

for letter in my_str:
    if letter == 'e':
        print('I found e')
        count_e += 1
    elif letter == 'm':
        print('I found m')
        count_m += 1
    else:
        print(letter)

print()        
print(f"number of e = {count_e}")
print(f"number of m = {count_m}")

