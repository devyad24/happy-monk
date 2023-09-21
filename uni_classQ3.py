class Student:
    existing_student_ids = {}

    def __init__(self, student_id, name):
        if not isinstance(student_id, int):
            raise ValueError("Student ID must be an integer.")
        if student_id in Student.existing_student_ids:
            raise ValueError("Student ID must be unique.")
        
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []
        Student.existing_student_ids[student_id] = True

    def add_course(self, course):
        self.enrolled_courses.append(course)
        course.enrolled_students.append(self)

    def remove_course(self, course):
        self.enrolled_courses.remove(course)
        course.enrolled_students.remove(self)

    def get_course_list(self):
        return [course.title for course in self.enrolled_courses]

class Course:
    existing_course_codes = {}

    def __init__(self, course_code, title, instructor, max_capacity):
        if not isinstance(course_code, str):
            raise ValueError("Course code must be a string.")
        if course_code in Course.existing_course_codes:
            raise ValueError("Course code must be unique.")

        self.course_code = course_code
        self.title = title
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_students = []
        Course.existing_course_codes[course_code] = True

    def enroll_student(self, student):
        if len(self.enrolled_students) < self.max_capacity:
            self.enrolled_students.append(student)
            student.add_course(self)

    def unenroll_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.remove_course(self)

    def get_student_list(self):
        return [student.name for student in self.enrolled_students]

    def is_full(self):
        return len(self.enrolled_students) >= self.max_capacity

class University:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

student1 = Student(1, "Alice")
student2 = Student(2, "Bob")
course1 = Course("CS101", "Introduction to Programming", "Prof. Smith", 30)
course2 = Course("MATH202", "Calculus II", "Prof. Johnson", 25)
university = University()

university.add_student(student1)
university.add_student(student2)
university.add_course(course1)
university.add_course(course2)

course1.enroll_student(student1)
course1.enroll_student(student2)
course2.enroll_student(student1)

print(student1.get_course_list())  
print(course1.get_student_list()) 
