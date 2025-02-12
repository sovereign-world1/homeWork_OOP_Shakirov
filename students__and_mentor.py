class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ratings = {}
        self.average_grade = 0
        self.student_list += [self]

    def add_courses(self, course_name):
            self.finished_courses += [course_name]
            self.courses_in_progress += [course_name]

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            average = sum(all_grades) / len(all_grades)
        else:
            average = 0
        return average
    
    def __ge__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.avr() >= best_lecturer.avr()
        else:
            return NotImplemented
        
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.avr():.2f}\n'
                f'Курсы в процессе изучения:{",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)} ')
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ratings = {}
        self.courses_attached = []  
        self.average_grade = 0
        self.grades = {}
        self.lecturer_list += [self]

    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            average = sum(all_grades) / len(all_grades)
        else:
            average = 0
        return average
    
    def __ge__(self, student):
        if isinstance(student, Student):
            return self.avr() >= best_student.avr()
        else:
            return NotImplemented
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avr():.2f} '

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['OOP']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
new_best_student = Student('Ilnur', 'Shakirov', 'male')
new_best_student.courses_in_progress += ['OOP']
new_best_student.courses_in_progress += ['Git']
new_best_student.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Git']
best_lecturer.courses_attached += ['OOP']
new_best_lecturer = Lecturer('Henry', 'Bond')
new_best_lecturer.courses_attached += ['OOP']
new_best_lecturer.courses_attached += ['Git']

cool_reviewer = Reviewer('Some', 'Duddy')
cool_reviewer.courses_attached += ['Python']
new_cool_reviewer = Reviewer('Rob', 'Chaky')
new_cool_reviewer.courses_attached += ['OOP']

best_student.rate_lec(best_lecturer, 'OOP', 10)
best_student.rate_lec(best_lecturer, 'OOP', 9)
best_student.rate_lec(best_lecturer, 'OOP', 8)

best_student.rate_lec(new_best_lecturer, 'Git', 9)
best_student.rate_lec(new_best_lecturer, 'Git', 7)
best_student.rate_lec(new_best_lecturer, 'Git', 8)

new_best_student.rate_lec(new_best_lecturer, 'Git', 8)
new_best_student.rate_lec(new_best_lecturer, 'Git', 10)
new_best_student.rate_lec(new_best_lecturer, 'Git', 9)



cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)

cool_reviewer.rate_hw(new_best_student, 'Git', 8)
cool_reviewer.rate_hw(new_best_student, 'Git', 9)
cool_reviewer.rate_hw(new_best_student, 'Git', 10)

new_cool_reviewer.rate_hw(new_best_student, 'OOP', 8)
new_cool_reviewer.rate_hw(new_best_student, 'OOP', 9)
new_cool_reviewer.rate_hw(new_best_student, 'OOP', 8)

if best_student.avr() >= best_lecturer.avr():
    print(f'{best_student.name}, больше чем, {best_lecturer.name}.')
else:
    print(f'{best_lecturer.name}, больше чем, {best_student.name}.')
print()
print(best_student)
print(new_best_student)
print()
print(best_lecturer)
print(new_best_lecturer)
print()
print(cool_reviewer)
print(new_cool_reviewer)

def avr_gr_students(students, course):
    student_courses = []
    for student in students:
        for k, v in student.grades.items():
            if k == course:
                student_courses.extend(v)
    summa = sum(student_courses)
    average_grade = float(summa / len(student_courses))
    return average_grade

def avr_gr_lectures(lecturers, course):
    lecture_courses = []
    for lecturer in lecturers:
        for a, b in lecturer.grades.items():
            if a == course:
                lecture_courses.extend(b)
    summa = sum(lecture_courses)
    average_grade = float(summa / max(len(lecture_courses), 1))
    return average_grade

print()
print(f'Средняя оценка для всех студентов по курсу {"OOP"}: {avr_gr_students(Student.student_list, 'OOP')}')
print()
print(f'Средняя оценка для всех лекторов по курсу {"OOP"}: {avr_gr_lectures(Lecturer.lecturer_list, 'OOP')}')