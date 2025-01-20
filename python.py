def show_best_mark_and_student(list):
    max_mark = 0
    best_student = ''
    
    for mark,stu in list:
        if mark > max_mark:
            max_mark = mark
            best_student = stu
            
    return best_student, max_mark

school = [(14,'anna'), (17,'ali'), (10,'mmd'), (18,'sara'), (19,'erfan')]

print(show_best_mark_and_student(school))
