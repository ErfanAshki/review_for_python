print('current grades !')

print('\n' + '-' * 20)

with open('grades.txt', 'r') as reader:
    print(reader.read())
    
new_grades = []

print('\n' + '-' * 20)

while True:
    yes_or_no_input = input('Do you want to add new grade ?')

    if yes_or_no_input in ['yes', 'no']:
        if yes_or_no_input == 'no':
            break
        elif yes_or_no_input == 'yes':
            while True:
                name_input = input('Enter your name : ')            
                    
                grade_input = input('Enter your grade :')
                try : 
                    new_grades.append({
                        'name': name_input,
                        'grade': float(grade_input)
                    })
                    break
                except ValueError:
                    print('You should Enter a number')
                    print('\n' + '-' * 20)
                    
            break
    else:
        print('Select from yes or no')
        print('\n' + '-' * 20)
               
            
with open('grades.txt', 'a') as grades_files:
    for stu_grade in new_grades:
        grades_files.write(f"\n{stu_grade['name']} {stu_grade['grade']}")       


with open('grades.txt', 'r') as avg_reader:
    all_avg_grades = avg_reader.read().split('\n')
    
    grades_list = []

    for line in all_avg_grades:
        x = line.split(' ')
        name = x[0]
        grade = x[1]
        
        grades_list.append(float(grade))
        
    print(sum(grades_list) / len(grades_list)) 
    
