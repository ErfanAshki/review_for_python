def calc_income(income):
    if income <= 0 : 
        assert income>0 , 'Income must be bigger than 0'
        
    return income * 2

try:
    print(calc_income(-55))
except Exception:
    print('Exception occurred')    

print('end')

