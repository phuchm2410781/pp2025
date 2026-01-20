import curses
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def input_box(stdscr,prompt):
    curses.echo()
    stdscr.addstr(prompt)
    stdscr.clrtoeol()
    value = stdscr.getstr().decode()
    curses.noecho()
    stdscr.addstr("\n")
    return value

def write_students(students,filename="student.txt"):
    path = os.path.join(BASE_DIR,filename)
    with open(filename, 'w', encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.student_id},{s.name},{s.dob}\n")

def write_courses(courses,filename="courses.txt"):
    path = os.path.join(BASE_DIR,filename)
    with open(filename, 'w', encoding='utf-8') as f:
        for c in courses:
            f.write(f"{c.course_id},{c.name},{c.credit}\n")

def write_marks(students,filename="marks.txt"):
    path = os.path.join(BASE_DIR,filename)
    with open(filename, 'w',encoding='utf-8') as f:
        for s in students:
            for course_id,mark in s.marks.items():
                f.write(f"{s.student_id},{course_id},{mark}\n")