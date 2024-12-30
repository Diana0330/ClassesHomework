# Problem 1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __student_existence__(self, courses_attached):
        for course in courses_attached:
            if course in self.finished_courses:
                return True
            if course in self.courses_in_progress:
                return True
        return False

    def feedback(self, lecturer, grade, course_name):
        if isinstance(lecturer, Lecturer) and self.__student_existence__(lecturer.courses_attached):
            if course_name in lecturer.lecture_grades:
                lecturer.lecture_grades[course_name] += [grade]
            else:
                lecturer.lecture_grades[course_name] = [grade]


# Problem 2
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        self.lecture_grades = {}
        super().__init__(name, surname)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


first_lecturer = Lecturer('Michael', 'Jones')
first_lecturer.courses_attached = ['Java', 'Databases', 'Web Design']
first_student = Student('John', 'Evans', 'male')
first_student.finished_courses = ['Java']
first_student.courses_in_progress = ['Databases']
first_student.feedback(first_lecturer, 9, 'Databases')
first_student.feedback(first_lecturer, 8, 'Databases')
print(first_lecturer.lecture_grades)

first_reviewer = Reviewer('Jane', 'August')
first_reviewer.courses_attached = ['Web Development', 'Databases', 'Data Analytics']
first_reviewer.rate_hw(first_student, 'Databases', 8)
print(first_student.grades)




