def check_even_numbers_in_list(list):
    even_num = []

    for num in list:
        if num % 2 == 0:
            even_num.append(num)

    return even_num


print(check_even_numbers_in_list([1,2,3,5,63,95,2,520,54]))
print(check_even_numbers_in_list([11,45,10,32,987,65,87,45,88]))
