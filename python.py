my_cryptography = '222,248,224,244,214,250,250,126,126'
my_list = []


for num in my_cryptography.split(",") :
    my_list.append(chr(int((int(num) - 20) / 2)))
   
    
print("".join(my_list))  

