my_str = 'tHis iS SomE SENtences'

def first_word_uppercase(str): 
    """"Return the upper case of first word of string"""

    def get_first_word(str):
        """"Return the first word of string"""
        return str.split()[0]
        
    str = get_first_word(str)
    return str.upper()

print(first_word_uppercase(my_str))
