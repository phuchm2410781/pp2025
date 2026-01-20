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