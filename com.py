list1 = [1,2,3]
list2 = ['a', 'b', 'c']
# combined = []

# for num in list1:
#     for letter in list2:
#         if num != letter:
#             combined.append((num, letter))
            
# print(combined)

combined = [(num, letter) for num in list1 for letter in list2 if num != letter]

print(combined)
