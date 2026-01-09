class Student:
    def __init__(self,student_id,name,dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.marks = {}
    def mark(self,course_id,mark):
        self.marks[course_id] = mark

class Course:
    def __init__(self, name, course_id):
        self.course_id = course_id
        self.name = name

class Manage:
    def __init__(self):
        self.student = []
        self.course = []
    def input_student(self):
        num = int(input("Enter number of students: "))
        for _ in range(num):
            sID = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth:")
            self.student.append(Student(sID,name,dob))
    def input_course(self):
        num = int(input("Enter number of courses: "))
        for _ in range(num):
            cID = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.course.append(Course(cID,name))
    def find_course(self,course_id):
        for course in self.course:
            if course.course_id == course_id:
                return course
        return None
    def input_mark(self):
        if not self.student:
            print("No student available.")
            return
        course_id = input("Enter course ID to mark: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        for student in self.student:
            mark = float(input(f"Enter mark for student {student.name}: "))
            student.mark(course_id,mark)

class ManagePrint(Manage):
    def print_student_list(self):
        print("\nStudent list:")
        for i in self.student:
            print(f"Name: {i.name} | ID: {i.student_id} | DoB: {i.dob}\n")
    def print_course_list(self):
        print("\nCourse list:")
        for i in self.course:
            print(f"Name: {i.name} | ID: {i.course_id}\n")
    def show_mark(self):
        course_id = input("Enter course ID: ")
        course = self.find_course(course_id)
        if not course:
            print("Course not found.")
            return
        print(f"Mark for {course.name}:\n")
        for student in self.student:
            mark = student.marks.get(course_id, "None")
            print(f"{student.name}: {mark}")

manager = ManagePrint()
manager.input_student()
manager.input_course()
manager.print_student_list()
manager.print_course_list()
manager.input_mark()
manager.show_mark()