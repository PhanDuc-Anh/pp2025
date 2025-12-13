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
