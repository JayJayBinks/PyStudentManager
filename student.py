class Student:
    students = []

    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        Student.students.append(self)

    def __str__(self):
        return "This is a student."

    @staticmethod
    def get_students():
        students_titlecase = []
        for student in Student.students:
            students_titlecase.append(student.name.title())
        return students_titlecase
