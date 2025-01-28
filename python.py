def calc_income(income):
    if income <= 0 : 
        raise Exception('Income must be bigger than 0')
        
    return income * 2

print(calc_income(-55))

print('end')
