def add_num(a):
    if a<3:
        return add_num(a+1)
    return a

print(add_num(1))
