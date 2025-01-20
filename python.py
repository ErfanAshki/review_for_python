def sum_and_sub_for_numbers(num1,num2):
    sum_result = num1 + num2
    sub_result = num1 - num2

    return (sum_result,sub_result)

print(sum_and_sub_for_numbers(5,3))
print(sum_and_sub_for_numbers(54,10))

(a,b) = sum_and_sub_for_numbers(44,50)
print(a)
print(b)
print(a,b)
