my_dict = {
    'key1': 55 , 
    'key2': 'hello world',
    'key3': [2, 'ss', 10, -77],
    'key4': {
        'a': 5,
        'b': [10,20,30],
        'c': 'khkhkdd'
    }
}

print(my_dict['key1'])
print(my_dict['key3'][0])
print(my_dict['key3'][-2: ])
print(my_dict['key4']['a'])
print(my_dict['key4']['c'])
print(my_dict['key4']['b'][1])

my_dict['key1'] = '55'

print(my_dict)
