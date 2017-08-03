_studentList = []


class Student:

    def __init__(self, forename, lastname, student_id):
        self.forename = forename
        self.lastname = lastname
        self.id = student_id

    def __str__(self):
        return "This is student {1} {2} with id {3}".format(self, self.forename, self.lastname, self.id)


def get_student_names():
        students_names = []
        for student in _studentList:
            students_names.append(student.forename + " " + student.lastname)
        return students_names


def add_student_to_list(student):
    return _studentList.append(student)


def get_student_list():
    return _studentList

