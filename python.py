def longest_string_and_len(*args):
    string_list = []
    user_input = input('Enter your string : ')
    string_list.append(user_input)
    
    while user_input != 'exit':
        user_input = input('Enter your string : ')
        string_list.append(user_input)
        
        longest_str = ''
        for str in string_list:
            if len(str) > len(longest_str):
                longest_str = str
        
    return longest_str , len(longest_str)
        
        
print(longest_string_and_len())