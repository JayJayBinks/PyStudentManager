students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)

while input("Do you want to add a student? (y/n)") == "y":
    add_student(input("Student name:"), input("Student id:"))

print("Current students are: {0}".format(students))
