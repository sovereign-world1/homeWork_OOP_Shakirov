class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
            self.finished_courses += [course_name]

    def rate_hw(self, lecturer, course, grade):
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
    
    def __ge__(self, lector):
        if isinstance(lector, Lecturer):
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
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            average = sum(all_grades) / len(all_grades)
        else:
            average = 0
        return average
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avr():.2f} '

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
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
new_best_lecturer = Lecturer('Henry', 'Bond')
new_best_lecturer.courses_attached += ['OOP']

cool_reviewer = Reviewer('Some', 'Duddy')
cool_reviewer.courses_attached += ['Python']
new_cool_reviewer = Reviewer('Rob', 'Chaky')
new_cool_reviewer.courses_attached += ['OOP']

new_best_student.rate_hw(best_lecturer, 'Git', 10)
best_student.rate_hw(new_best_lecturer, 'OOP', 9)
best_student.rate_hw(best_lecturer, 'Git', 8)

new_cool_reviewer.rate_hw(new_best_student, 'OOP', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)

print(best_student)
print(new_best_student)
print()
print(best_lecturer)
print(new_best_lecturer)
print()
print(cool_reviewer)
print(new_cool_reviewer)