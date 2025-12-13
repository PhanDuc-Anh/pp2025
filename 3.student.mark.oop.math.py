import math
import numpy
import curses

class Student():
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__gpa = 0

    def get_gpa(self):
        return self.__gpa
    def get_name_student(self):
        return self.__name
    def get_id_student(self):
        return self.__id
    def get_dob_student(self):
        return self.__dob

    def set_gpa(self, gpa):
        self.__gpa = gpa


class Course():
    def __init__(self, name, id, credit):
        self.__name = name
        self.__id = id
        self.__credit = credit

    def get_name_course(self):
        return self.__name
    def get_id_course(self):
        return self.__id
    def get_credit_course(self):
        return self.__credit


class Sys():
    def __init__(self, stdscr):
        self.__students = []
        self.__courses = []
        self.__marks = {}
        self.stdscr = stdscr

    def get_screen_size(self):
        return self.stdscr.getmaxyx()

    def center_text(self, y, text, attr=0):
        h, w = self.get_screen_size()
        x = max(0, w // 2 - len(text) // 2)
        if y < h and x < w:
            self.stdscr.addstr(y, x, text[:w-x], attr)

    def get_input(self, y, prompt):
        h, w = self.get_screen_size()
        x = max(0, w // 2 - len(prompt) // 2)
        if y < h:
            self.stdscr.addstr(y, x, prompt)
            self.stdscr.refresh()
            curses.echo()
            curses.curs_set(1)
            input_x = x + len(prompt)
            if input_x < w:
                user_input = self.stdscr.getstr(y, input_x, 50).decode('utf-8')
            else:
                user_input = ""
            curses.noecho()
            curses.curs_set(0)
            return user_input
        return ""

    def display_centered(self, lines, title=""):
        self.stdscr.clear()
        h, w = self.get_screen_size()

        total_lines = len(lines) + (2 if title else 0)
        start_y = max(0, h // 2 - total_lines // 2)

        if title:
            self.center_text(start_y, "=" * (len(title) + 4), curses.A_BOLD)
            self.center_text(start_y + 1, f"  {title}  ", curses.A_BOLD)
            self.center_text(start_y + 2, "=" * (len(title) + 4), curses.A_BOLD)
            start_y += 4

        for i, line in enumerate(lines):
            if start_y + i < h:
                self.center_text(start_y + i, line)

        self.stdscr.refresh()
        return start_y + len(lines)

    def wait_for_key(self, y=None):
        h, w = self.get_screen_size()
        if y is None:
            y = h - 2
        msg = "Press any key to continue..."
        self.center_text(y + 2, msg, curses.A_DIM)
        self.stdscr.refresh()
        self.stdscr.getch()

    def input_course(self):
        self.stdscr.clear()
        h, w = self.get_screen_size()
        start_y = h // 2 - 5

        self.center_text(start_y, "=== Input Courses ===", curses.A_BOLD)

        try:
            num_courses = int(self.get_input(start_y + 2, "Enter the number of courses: "))

            for i in range(num_courses):
                self.stdscr.clear()
                self.center_text(start_y, f"=== Course {i + 1} of {num_courses} ===", curses.A_BOLD)

                course_id = self.get_input(start_y + 2, "Enter course ID: ")
                course_name = self.get_input(start_y + 3, "Enter course name: ")
                course_credit = int(self.get_input(start_y + 4, "Enter course credit: "))
                self.__courses.append(Course(course_name, course_id, course_credit))

            self.stdscr.clear()
            self.center_text(h // 2, "Courses added successfully!", curses.A_BOLD)
            self.wait_for_key(h // 2)
        except ValueError:
            self.stdscr.clear()
            self.center_text(h // 2, "Input error - please enter valid numbers", curses.A_BOLD)
            self.wait_for_key(h // 2)

    def input_student(self):
        self.stdscr.clear()
        h, w = self.get_screen_size()
        start_y = h // 2 - 5

        self.center_text(start_y, "=== Input Students ===", curses.A_BOLD)

        try:
            num_students = int(self.get_input(start_y + 2, "Enter the number of students: "))

            for i in range(num_students):
                self.stdscr.clear()
                self.center_text(start_y, f"=== Student {i + 1} of {num_students} ===", curses.A_BOLD)

                student_id = self.get_input(start_y + 2, "Enter student ID: ")
                student_name = self.get_input(start_y + 3, "Enter student name: ")
                student_dob = self.get_input(start_y + 4, "Enter student DOB: ")
                self.__students.append(Student(student_name, student_id, student_dob))

            self.stdscr.clear()
            self.center_text(h // 2, "Students added successfully!", curses.A_BOLD)
            self.wait_for_key(h // 2)
        except ValueError:
            self.stdscr.clear()
            self.center_text(h // 2, "Input error - please enter valid data", curses.A_BOLD)
            self.wait_for_key(h // 2)

    def input_marks(self):
        self.stdscr.clear()
        h, w = self.get_screen_size()

        if not self.__students:
            self.center_text(h // 2, "No students available", curses.A_BOLD)
            self.wait_for_key(h // 2)
            return
        if not self.__courses:
            self.center_text(h // 2, "No courses available", curses.A_BOLD)
            self.wait_for_key(h // 2)
            return

        lines = ["Choose a course for mark input:", ""]
        for i, course in enumerate(self.__courses):
            lines.append(f"{i + 1}: {course.get_name_course()} ({course.get_id_course()})")

        end_y = self.display_centered(lines, "Input Marks")

        try:
            course_choice = int(self.get_input(end_y + 1, "Make your choice: "))
            if course_choice < 1 or course_choice > len(self.__courses):
                self.stdscr.clear()
                self.center_text(h // 2, "Invalid choice", curses.A_BOLD)
                self.wait_for_key(h // 2)
                return

            selected_course_id = self.__courses[course_choice - 1].get_id_course()
            self.__marks[selected_course_id] = {}

            for student in self.__students:
                self.stdscr.clear()
                self.center_text(h // 2 - 2, f"=== Entering marks for {self.__courses[course_choice - 1].get_name_course()} ===", curses.A_BOLD)
                mark_str = self.get_input(h // 2, f"Enter marks for {student.get_name_student()}: ")
                mark = math.floor(float(mark_str) * 10) / 10
                self.__marks[selected_course_id][student.get_id_student()] = mark

            self.stdscr.clear()
            self.center_text(h // 2, "Marks added successfully!", curses.A_BOLD)
            self.wait_for_key(h // 2)
        except ValueError:
            self.stdscr.clear()
            self.center_text(h // 2, "Input error - please enter valid numbers", curses.A_BOLD)
            self.wait_for_key(h // 2)

    def cal_gpa(self):
        if not self.__students or not self.__courses:
            return

        for student in self.__students:
            mark = []
            credit = []
            for course in self.__courses:
                if course.get_id_course() in self.__marks and student.get_id_student() in self.__marks[course.get_id_course()]:
                    mark.append(self.__marks[course.get_id_course()][student.get_id_student()])
                    credit.append(course.get_credit_course())
            if not mark:
                student.set_gpa(0)
                continue

            if credit:
                gpa = numpy.average(mark, weights=credit)
            else:
                gpa = numpy.average(mark)
            student.set_gpa(gpa)

    def list_marks(self):
        self.stdscr.clear()
        h, w = self.get_screen_size()

        if not self.__courses:
            self.center_text(h // 2, "No courses available", curses.A_BOLD)
            self.wait_for_key(h // 2)
            return

        lines = ["Choose a course to view marks:", ""]
        for i, course in enumerate(self.__courses):
            lines.append(f"{i + 1}: {course.get_name_course()} ({course.get_id_course()})")

        end_y = self.display_centered(lines, "View Marks")

        try:
            course_choice = int(self.get_input(end_y + 1, "Make your choice: "))
            if course_choice < 1 or course_choice > len(self.__courses):
                self.stdscr.clear()
                self.center_text(h // 2, "Invalid choice", curses.A_BOLD)
                self.wait_for_key(h // 2)
                return

            selected_course = self.__courses[course_choice - 1].get_id_course()
            self.stdscr.clear()

            if selected_course in self.__marks:
                lines = []
                course_marks = self.__marks[selected_course]
                for student in self.__students:
                    mark = course_marks.get(student.get_id_student(), "N/A")
                    lines.append(f"{student.get_name_student()} ({student.get_id_student()}): {mark}")

                end_y = self.display_centered(lines, f"Marks for {self.__courses[course_choice - 1].get_name_course()}")
                self.wait_for_key(end_y)
            else:
                self.center_text(h // 2, "No marks recorded for this course", curses.A_BOLD)
                self.wait_for_key(h // 2)
        except ValueError:
            self.stdscr.clear()
            self.center_text(h // 2, "Input error", curses.A_BOLD)
            self.wait_for_key(h // 2)

    def list_course(self):
        self.stdscr.clear()
        h, w = self.get_screen_size()

        if not self.__courses:
            self.center_text(h // 2, "No courses available", curses.A_BOLD)
            self.wait_for_key(h // 2)
        else:
            lines = []
            for course in self.__courses:
                lines.append(f"Name: {course.get_name_course()} | ID: {course.get_id_course()} | Credits: {course.get_credit_course()}")

            end_y = self.display_centered(lines, "Course List")
            self.wait_for_key(end_y)

    def list_student(self):
        self.stdscr.clear()
        h, w = self.get_screen_size()

        if not self.__students:
            self.center_text(h // 2, "No students available", curses.A_BOLD)
            self.wait_for_key(h // 2)
        else:
            self.cal_gpa()
            self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

            lines = []
            for student in self.__students:
                lines.append(f"{student.get_name_student()} | ID: {student.get_id_student()} | DOB: {student.get_dob_student()} | GPA: {student.get_gpa():.2f}")

            end_y = self.display_centered(lines, "Student List (Sorted by GPA)")
            self.wait_for_key(end_y)


def draw_menu(stdscr, current_row):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    menu = [
        "Input Student Info",
        "Input Course Info",
        "Input Marks",
        "List Students",
        "List Courses",
        "List Marks",
        "Exit"
    ]

    title = "School System Terminal"
    title_y = h // 2 - len(menu) // 2 - 4

    stdscr.addstr(title_y, w // 2 - len(title) // 2 - 2, "=" * (len(title) + 4), curses.A_BOLD)
    stdscr.addstr(title_y + 1, w // 2 - len(title) // 2 - 1, f" {title} ", curses.A_BOLD)
    stdscr.addstr(title_y + 2, w // 2 - len(title) // 2 - 2, "=" * (len(title) + 4), curses.A_BOLD)

    for idx, item in enumerate(menu):
        x = w // 2 - len(item) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == current_row:
            stdscr.addstr(y, x - 2, f"> {item} <", curses.A_REVERSE | curses.A_BOLD)
        else:
            stdscr.addstr(y, x, item)

    hint = "Use UP/DOWN arrows to navigate, ENTER to select"
    stdscr.addstr(h - 2, w // 2 - len(hint) // 2, hint, curses.A_DIM)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    terminal = Sys(stdscr)
    current_row = 0

    while True:
        draw_menu(stdscr, current_row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 6:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                terminal.input_student()
            elif current_row == 1:
                terminal.input_course()
            elif current_row == 2:
                terminal.input_marks()
            elif current_row == 3:
                terminal.list_student()
            elif current_row == 4:
                terminal.list_course()
            elif current_row == 5:
                terminal.list_marks()
            elif current_row == 6:
                stdscr.clear()
                h, w = stdscr.getmaxyx()
                msg = "Mayonnaise on the escalator, it's going upstairs, so see ya later!"
                stdscr.addstr(h // 2, w // 2 - len(msg) // 2, msg, curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()
                break


if __name__ == "__main__":
    curses.wrapper(main)
