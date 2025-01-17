first_names = ['john', 'sara', 'hadi', 'mahtab']
last_names = ['smith', 'babaki']
age = [10,22,19]

for item in zip(first_names,last_names,age):
    print(item)

for first,last,age  in zip(first_names,last_names,age):
    print(age)
    print(last, first)

    