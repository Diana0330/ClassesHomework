# Problem 1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    # Problem 2

    def __student_existence(self, courses_attached):
        for course in courses_attached:
            if course in self.finished_courses:
                return True
            if course in self.courses_in_progress:
                return True
        return False
    # Problem 2

    def feedback(self, lecturer, grade, course_name):
        if isinstance(lecturer, Lecturer) and self.__student_existence(lecturer.courses_attached):
            if course_name in lecturer.lecture_grades:
                lecturer.lecture_grades[course_name] += [grade]
            else:
                lecturer.lecture_grades[course_name] = [grade]

    # Problem 3.1

    def average_grade(self):
        summa = 0
        counter = 0
        for grade in self.grades.values():
            summa += sum(grade)
            counter += len(grade)
        if counter != 0:
            return summa/counter
        else:
            return 0

    # Problem 3.1
    def __str__(self):
        return f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
        f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n' \
        f'Завершенные курсы: {', '.join(self.finished_courses)}'

    # Problem 3.2
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

# Problem 1
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Problem 1
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Problem 1
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        self.lecture_grades = {}
        super().__init__(name, surname)

    def average_grade(self):
        summa = 0
        counter = 0
        for grade in self.lecture_grades.values():
            summa += sum(grade)
            counter += len(grade)
        if counter != 0:
            return summa/counter
        else:
            return 0

    # Problem 3.2
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


    # Problem 3.1

    def __str__(self):
        return f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}\n' \
        f'Средняя оценка за за лекции: {self.average_grade()}'


# Problem 1
class Reviewer(Mentor):
# Problem 2
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Problem 3.1

    def __str__(self):
        return f'Имя: {self.name}\n' \
        f'Фамилия: {self.surname}'


#Problem 4

def average_grade(student_list, course_name):
    summa = 0
    counter = 0
    for student in student_list:
        grade = student.grades.get(course_name)
        if grade is not None:
            summa += sum(grade)
            counter += len(grade)
    if counter != 0:
        return summa / counter
    else:
        return 0


def lecture_average_grade(lecture_list, course_name):
    summa = 0
    counter = 0
    for lecture in lecture_list:
        grade = lecture.lecture_grades.get(course_name)
        if grade is not None:
            summa += sum(grade)
            counter += len(grade)
    if counter != 0:
        return summa / counter
    else:
        return 0


first_student = Student('John', 'Evans', 'male')
second_student = Student('John', 'Bates', 'male')
third_student = Student('Peter', 'Parker', 'male')
first_lecturer = Lecturer('Michael', 'Jones')
second_lecturer = Lecturer('James', 'Dean')
third_lecturer = Lecturer('Sandra', 'Bullock')
first_reviewer = Reviewer('Jane', 'August')
second_reviewer = Reviewer('Bryan', 'Adams')
course_name = 'Python for Beginners'
course_name_second = 'Fundamentals of JavaScript'
# first_student.finished_courses = ['Java']
first_student.courses_in_progress = [course_name, course_name_second]
second_student.courses_in_progress = [course_name, course_name_second]
third_student.courses_in_progress = [course_name, course_name_second]
courses_attached = [course_name, course_name_second]
first_lecturer.courses_attached = [course_name, course_name_second]
second_lecturer.courses_attached = [course_name, course_name_second]
third_lecturer.courses_attached = [course_name, course_name_second]
first_reviewer.courses_attached = [course_name, course_name_second]
second_reviewer.courses_attached = [course_name, course_name_second]

# third_student.finished_courses = ['Javascript']
# third_student.courses_in_progress = ['POSTGRESSQL']

first_student.feedback(first_lecturer, 9, course_name)
first_student.feedback(first_lecturer, 8, course_name_second)
first_student.feedback(second_lecturer, 8, course_name)
first_student.feedback(second_lecturer, 9, course_name_second)
second_student.feedback(third_lecturer,10, course_name)
first_reviewer.rate_hw(first_student, course_name, 8)
first_reviewer.rate_hw(third_student,course_name_second, 5)
second_reviewer.rate_hw(second_student, course_name, 8)
first_reviewer.rate_hw(second_student, course_name_second, 5)
print(second_student == first_student)
print(first_student == third_student)
print(first_lecturer == second_lecturer)
print(first_lecturer == third_lecturer)
#print(first_lecturer.lecture_grades)
#print(first_student.grades)
print(first_student)
print(first_lecturer)
print(first_reviewer)
print(second_student)
print(third_student)
print(second_lecturer)
print(third_lecturer)
print(first_reviewer)
print(second_reviewer, sep='\n\n')
student_list = [first_student, second_student, third_student]
average_grades_total = average_grade(student_list, course_name)
print(f'The average grade for all students for the course is: {average_grades_total}', sep='\n\n')
lecture_list = [first_lecturer, second_lecturer, third_lecturer]
lecture_average_grades_total = lecture_average_grade(lecture_list, course_name)
print(f'The average grade for all lecturers for the course is: {lecture_average_grades_total}', sep='\n\n')


