def some_keys(*args , **kwargs):    
    return kwargs , args


print(some_keys(25, 'swift', a=1, b='agile', ss='nimble', q=10))