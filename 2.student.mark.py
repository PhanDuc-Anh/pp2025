class Student():
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob

    def get_name_student(self):
        return self.__name
    def get_id_student(self):
        return self.__id
    def get_dob_student(self):
        return self.__dob


class Course():
    def __init__(self, name, id):
        self.__name = name
        self._id = id

    def get_name_course(self):
        return self.__name
    def get_id_course(self):
        return self.__id


class School():
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
    
    def input_course(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.__courses.append(Course(course_name, course_id))

    def input_student(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            self.__students.append(Student(student_name, student_id, student_dob))
    
    def input_marks(self):
        if not self.__students:
            print("No students")
            return
        if not self.__courses:
            print("No courses")
            return
        
        print("Choose a course for mark input: ")
        for i, course in enumerate(self.__courses):
            print(f"{i + 1}: {course.get_name_course()} ({course.get_id_course()})")
        try:
            course_choice = int(input("Make your choice mortal: "))
            if course_choice < 0 or course_choice > len(self.__courses):
                print("Value is lol (invalid)")
                return
            selected_course_id = self.__courses[course_choice - 1].get_id_course()
            self.__marks[selected_course_id] = {}
            for student in self.__students:
                mark = float(input(f"Enter marks for {student.get_name_student()}:"))
                self.__marks[selected_course_id][student.get_id_student()] = mark
        except ValueError:
            print("Input error")
    
    def list_marks(self):
        print("Enter a course to view its marks:")
        for i, course in enumerate(self.__courses):
            print(f"{1 + i}: {course.get_name_course()} ({course.get_id_course()})")
        try:
            course_choice = int(input("Make your choice creature: "))
            if course_choice < 0 or course_choice > len(self.__courses):
                print("Value is lol (invalid)")
                return
            selected_course = self.__courses[course_choice - 1].get_id_course()
            if selected_course in self.__marks:
                print(f"Marks of {self.__courses[course_choice].get_name_course()}")
                course_marks = self.__marks[selected_course.get_id()]
                for student in self.__students:
                    mark = course_marks.get(student.get_id_student())
                    print(f"Student: {student.get_name_student()} ({student.get_id.student()}) => {mark}")
            else:
                print("Course have no data")
        except ValueError:
            print("Input error")

    def list_course(self):
        if not self.__courses:
            print("No courses")
            return
        else:
            for course in self.__courses:
                print(f"Name: {course.get_name_course()} - ID: {course.get_id_course()}")

    def list_student(self):
        if not self.__students:
            print("No students")
            return
        else:
            for student in self.__students:
                print(f"Name: {student.get_name_student()} - ID: {student.get_id_student()} - DOB: {student.get_dob_student()}")


def main():
    school = School()
    while True:
        print("""
== School sys terminal (i think) ==
1: Input student info
2: Input course info
3: Input marks
4: List student info
5: List course info
6: List marks
7: Exit (you don't appreciate my work >;c)
""")
        get = input("Make your decision: ")
        if get == '1':
            school.input_student()
        elif get == '2':
            school.input_course()
        elif get == '3':
            school.input_marks()
        elif get == '4':
            school.list_student()
        elif get == '5':
            school.list_course()
        elif get == '6':
            school.list_marks()
        elif get == '7':
            print("Mayonnaise on the escalator, it's going upstairs, so see ya later!")
            break
        else:
            print("You moron be making stupid input(s)")

if __name__ == "__main__":
    main()