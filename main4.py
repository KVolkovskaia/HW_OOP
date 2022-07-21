class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw(self):
        for index in self.grades.values():
            return(round(sum(index)/len(index),2))

    def __str__(self):
        res = f'''Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_hw()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}'''
        return res

    def __lt__(self, other):
        return self.average_hw() < other.average_hw()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self): 
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_lect(self):
        for index in self.grades.values():
            return(round(sum(index)/len(index),2))

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_lect()}'
        return res

    def __lt__(self, other):
        return self.average_lect() < other.average_lect()



student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']

student2 = Student('Kris', 'Nor', 'your_gender')
student2.courses_in_progress += ['Python', 'Git']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 8)

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Kim', 'Neman')
lecturer2.courses_attached += ['Python']

student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Python', 5)
student1.rate_lecture(lecturer2, 'Python', 4)
student1.rate_lecture(lecturer2, 'Python', 6)


students = [student1, student2]
lecturers = [lecturer1, lecturer2]

def average_grade(list, course):
    grades_all = []
    for current_student in list:
        for key, value in current_student.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    average_grades = round(sum(grades_all) / len(grades_all), 2)
    if list == students:
        print(f'Средняя оценка для всех студентов по курсу "Python": {average_grades}')
    if list == lecturers:
        print(f'Средняя оценка для всех лекторов по курсу "Python": {average_grades}')

print(student1)
print()
print(student2)
print()
print(student1 < student1)
print()
print(reviewer1)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(lecturer1 < lecturer2)
print()
average_grade(lecturers, 'Python')
print()
average_grade(students, 'Phyton')