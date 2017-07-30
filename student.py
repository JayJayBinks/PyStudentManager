_studentList = []


class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id

    def __str__(self):
        return "This is a student."


def get_students():
    return _studentList


def add_student(student):
    return _studentList.append(student)

