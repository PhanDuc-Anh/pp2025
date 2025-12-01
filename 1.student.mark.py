students = []
courses = []
marks = {}

def inputing():
    student_count = int(input("Enter the number of students: "))
    for _ in range(student_count):
        st_name = input("Enter student name: ")
        st_id = input("Enter student ID: ")
        st_dob = input("Enter student date of birth (dd/mm/yy): ")
        students.append({"name": st_name, "id": st_id, "dob": st_dob})

    course_count = int(input("Enter the number of courses: "))
    for _ in range(course_count):
        course_name = input("Enter course name: ")
        course_id = input("Enter course ID: ")
        courses.append({"name": course_name.lower(), "id": course_id})

    course_choice = input("Enter a course for input-ing marks: ")
    course_found = False
    for name in courses:
        if name["name"] == course_choice.lower():
            course_found = True
            marks[name["id"]] = {}
            print("Enter the marks for each student: ")
            for student in students:
                while True:
                    try:
                        mark_input = input(f"Enter mark for {student['id']}: ")
                        mark = float(mark_input)
                        marks[name["id"]][student["id"]] = mark
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number for the mark.")
            break
    
    if not course_found:
        print("Course not found.")

def listing():
    def listing_students():
        if not students:
            print("No students in the database")
            return
        for student in students:
            print(f"Name: {student["name"]}, ID: {student["id"]}, DOB: {student["dob"]}")

    def listing_courses():
        if not courses:
            print("No courses in the database")
            return
        for course in courses:
            print(f"Name: {course["name"]}, ID: {course["id"]}")

    def listing_marks():
        course_choice = input("Enter a course for listing marks: ")
        for name in courses:
            if name["name"] == course_choice.lower():
                for mark in marks[name["id"]]:
                    print(f"Student ID: {mark}, Mark: {marks[name["id"]][mark]}")
            else:
                print("Course does not exist in the database")

    print("""Choices given (pick a number corresponding to its option):
            1. List students
            2. List courses
            3. List marks
            4. List all
            5. Back""")
    to_list = int(input("Enter a choice: "))
    if to_list == 1:
        listing_students()
    elif to_list == 2:
        listing_courses()
    elif to_list == 3:
        listing_marks()
    elif to_list == 4:
        listing_students()
        listing_courses()
        listing_marks()
    elif to_list == 5:
        return

def main():
    while True:
        print("""Choices given (pick a number corresponding to its option):
            1. Enter data (students, courses, marks)
            2. List data
            3. Exit""")
        
        choice = int(input("Now make one (choice): "))
        if choice == 1:
            inputing()
        elif choice == 2:
            listing()
        elif choice == 3:
            break
        else:
            print("Re-enter a valid choice") #why are you "blind"?

if __name__ == "__main__":
    main()