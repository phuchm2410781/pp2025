import curses
from input import input_box
from output import draw
from domains import Student, Course, Manage
from persistence import save, load

class UI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        
        loaded = load()
        if loaded:
            self.manager = loaded
        else:
            self.manager = Manage()

    def add_student(self):
        sid = input_box(self.stdscr, "Enter student ID: ")
        name = input_box(self.stdscr, "Enter name: ")
        dob = input_box(self.stdscr, "Enter date of birth: ")

        self.manager.student.append(Student(sid, name, dob))
        save(self.manager)

    def add_course(self):
        cid = input_box(self.stdscr, "Enter course ID: ")
        cname = input_box(self.stdscr, "Enter course name: ")
        if not cname:
            return

        credit = int(input_box(self.stdscr, "Enter credit: "))
        self.manager.course.append(Course(cid, cname, credit))

        for s in self.manager.student:
            mark = float(input_box(self.stdscr, f"Mark for {s.name}: "))
            s.add_mark(cid, mark)

        save(self.manager)

    def input_mark(self):
        cid = input_box(self.stdscr, "Enter course ID: ")
        course = self.manager.find_course(cid)
        if not course:
            return

        for s in self.manager.student:
            mark = float(input_box(self.stdscr, f"Mark for {s.name}: "))
            s.add_mark(cid, mark)

        save(self.manager)

    def show_students(self):
        self.manager.calc_all_gpa()
        self.manager.sort_by_gpa_desc()

        lines = ["Student list sorted by GPA", "-" * 20]
        for s in self.manager.student:
            lines.append(f"{s.name} | GPA: {s.gpa}")

        draw(self.stdscr, lines)
        self.stdscr.getch()

    def menu(self):
        while True:
            draw(self.stdscr, [
                "STUDENT MANAGEMENT SYSTEM",
                "1. Add student",
                "2. Add course",
                "3. Input marks",
                "4. Show students by GPA",
                "5. Exit",
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

if __name__ == "__main__":
    curses.wrapper(main)
