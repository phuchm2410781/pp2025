import math
import numpy as np

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