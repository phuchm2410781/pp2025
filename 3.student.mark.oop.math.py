import math
import numpy as np
import curses

class Student:
    def __init__(self,student_id,name,dob):
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0
    def add_mark(self,course_id,mark):
        mark = math.floor(mark*10)/10
        self.marks[course_id] = mark
    def calc_gpa(self,courses):
        marks = []
        credits = []

        for c in courses:
            if c.course_id in self.marks:
                marks.append(self.marks[c.course_id])
                credits.append(c.credit)
        
        if not marks:
            self.gpa = 0.0
            return self.gpa
        
        marks = np.array(marks)
        credits = np.array(credits)

        self.gpa = np.sum(marks*credits)/np.sum(credits)
        self.gpa = round(self.gpa,2)
        return self.gpa

class Course:
    def __init__(self, course_id,name,credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

class Manage:
    def __init__(self):
        self.student = []
        self.course = []
    def find_course(self,course_id):
        for course in self.course:
            if course.course_id == course_id:
                return course
        return None
    def calc_all_gpa(self):
        for s in self.student:
            s.calc_gpa(self.course)
    
    def sort_by_gpa_desc(self):
        self.student.sort(key = lambda s:s.gpa, reverse=True)

class UI:
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.manager = Manage()
    
    def draw(self,lines):
        self.stdscr.clear()
        for i, line in enumerate(lines):
            self.stdscr.addstr(i,0,line)
        self.stdscr.refresh()
    
    def input_box(self,prompt):
        curses.echo()
        self.stdscr.addstr(prompt)
        self.stdscr.clrtoeol()
        value = self.stdscr.getstr().decode()
        curses.noecho()
        self.stdscr.addstr("\n")
        return value
    
    def add_student(self):
        sid = self.input_box("Enter student ID: ")
        name = self.input_box("Enter name: ")
        dob = self.input_box("Enter date of birth: ")
        self.manager.student.append(Student(sid,name,dob))
    
    def add_course(self):
        cid = self.input_box("Enter course ID: ")
        cname = self.input_box("Enter course name: ")
        if not cname:
            return
        credit = int(self.input_box("Enter credit: "))
        self.manager.course.append(Course(cid, cname, credit))

        for s in self.manager.student:
            mark = float(self.input_box(f"Mark for {s.name}: "))
            s.add_mark(cid, mark)


    def input_mark(self):
        cid = self.input_box("Enter course ID:")
        course = self.manager.find_course(cid)
        if not course:
            return
        
        for s in self.manager.student:
            mark = float(self.input_box(f"Mark for {s.name}: "))
            s.add_mark(cid,mark)

    def show_students(self):
        self.manager.calc_all_gpa()
        self.manager.sort_by_gpa_desc()
    
        lines = ["Student list sort by GPA", "-" * 20]
        for s in self.manager.student:
            lines.append(f"{s.name} | GPA: {s.gpa}")
        self.draw(lines)
        self.stdscr.getch()
    
    def menu(self):
        while True:
            self.draw([
                "STUDENT MANAGEMENT SYSTEM",
                "1.Add student",
                "2.Add course",
                "3.Input marks",
                "4.Show students by GPA",
                "5.Exit",
                "Choose an option: "
            ])
            option = self.stdscr.getch()
            if option == ord('1'):
                self.add_student()
            elif option == ord('2'):
                self.add_course()
            elif option == ord('3'):
                self.input_mark()
            elif option == ord('4'):
                self.show_students()
            elif option == ord('5'):
                break

def main(stdscr):
    curses.curs_set(0)
    ui = UI(stdscr)
    ui.menu()

curses.wrapper(main)