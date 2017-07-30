from PyStudentManager.student import Student, get_students
from PyStudentManager.file_helper import FileHelper

FileHelper.read_students()

print("Current students are: {0}".format(get_students()))

while input("Do you want to add a student? (y/n)") == "y":
    Student(input("Student name:"), input("Student id:"))

FileHelper.save_students()
