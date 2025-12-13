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
