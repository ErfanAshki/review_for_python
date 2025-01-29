a = 10

try : 
    print(a/0)
except ZeroDivisionError:
    print('Zero error')
except ModuleNotFoundError:
    print('Module error')
else:
    print('Code is ok')

print('End')
    

a = 10

try : 
    print(a/10)
except ZeroDivisionError:
    print('Zero error')
except ModuleNotFoundError:
    print('Module error')
else:
    print('Code is ok')

print('End')
