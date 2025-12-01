def input_numStu():
    stuNum = int(input("Enter number of students:"))
    return stuNum

def create_stuList(stuNum):
    StuList = {}
    for i in range(stuNum):
        StuList[i] = input(f"Enter information of #{i+1} student (id, name, DoB):")
    return StuList

def create_courseList():
    courseNum = int(input("Enter number of courses:"))
    courseList = {}
    for i in range(courseNum):
        courseList[i] = input(f"Enter course #{i+1} id and name:")
    return courseList

def mark(courseList,stuNum):
    chooseCourse = int(input("Enter course id to mark:"))
    stuMark = {}
    for i in range(stuNum):
        stuMark[i] = input(f"Enter student #{i+1} mark in the course {courseList[chooseCourse-1]}:")
    return stuMark

def print_coursesList(courseList):
    print("\nCourses list:(id,name)")
    for i in courseList:
        print(f"{courseList[i]}")

def print_studentList(stuList):
    print("\nStudent list:(id, name, DoB)")
    for i in stuList:
        print(f"{stuList[i]}")

def print_MarkList(stuMark):
    print("\nStudent mark for given courses:")
    for i in stuMark:
        print(f"{stuMark[i]}")

stuNum = input_numStu()
StuList = create_stuList(stuNum)
courseList = create_courseList()
listMark = mark(courseList,stuNum)
print_studentList(StuList)
print_coursesList(courseList)
print_MarkList(listMark)