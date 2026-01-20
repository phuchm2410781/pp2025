import curses
from input import input_box
from output import draw
from Domains import Student, Course, Manage

class UI:
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.manager = Manage()

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