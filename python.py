my_password = 'erfpass55'
my_list = []


for i in my_password:
    my_list.append(str(ord(i) * 2 + 20))
    
print(','.join(my_list))
print(type(','.join(my_list)))
    