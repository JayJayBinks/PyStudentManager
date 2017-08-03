from PyStudentManager.student import Student, get_student_names, add_student_to_list
from PyStudentManager.file_helper import FileHelper

FileHelper.read_students()

print("Current students are: {0}".format(get_student_names()))

while input("Do you want to add a student? (y/n)") == "y":
    new_student = Student(input("Student forename:"),input("Student lastname:"), input("Student id:"))
    add_student_to_list(new_student)
    FileHelper.save_student(new_student.__dict__)
