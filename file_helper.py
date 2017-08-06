from PyStudentManager.student import Student, get_student_names, add_student_to_list
import os
import json


class FileHelper:
    student_file = os.path.dirname(os.path.abspath(__file__)) + "\students.json"

    @staticmethod
    def save_student(student_dictionary):
        try:
            f = open(FileHelper.student_file, "a")
            f.write(json.dumps(student_dictionary)+"\n")
        except Exception as e:
            print("Could not write to file! Exception: {}".format(e))
        finally:
            f.close()

    @staticmethod
    def read_students():
        try:
            f = open(FileHelper.student_file, "r")
            for student in f.readlines():
                json_data = json.loads(student)
                add_student_to_list(Student(json_data["forename"], json_data["lastname"], json_data["id"]))
            f.close()
        except Exception as e:
            print("Could not read from file! Exception: {}".format(e))
