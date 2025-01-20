def show_longest_string_in_list(list):
    final_str = ''
    
    for str in list:
        if len(str) > len(final_str):
            final_str = str

    return final_str, len(final_str)

my_list = ['subtract', 'subtraction', 'subtracter', 'subtractive']

print(show_longest_string_in_list(my_list))

print()

max_str , max_str_len = show_longest_string_in_list(my_list)
print(max_str)
print(max_str_len)
print(max_str, max_str_len)
