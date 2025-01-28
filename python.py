def calc_income(income):
    if income <= 0 : 
        raise Exception('Income must be bigger than 0')
        
    return income * 2

try:
    print(calc_income(-55))
except:
    print('Exception occurred')    

print('end')

