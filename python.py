with open('grades.txt', 'r') as reader , open('result.txt', 'w') as writer:
    data = reader.read()
    writer.write(data)
    
