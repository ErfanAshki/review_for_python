import pickle

names = None

with open('name.txt', 'rb') as f:
    names = pickle.load(f)
    

print(names)
