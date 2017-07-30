from PyStudentManager.student import Student, get_students, add_student


class FileHelper:
    student_file = "students.txt"

    @staticmethod
    def save_students():
        try:
            f = open(FileHelper.student_file, "w")
            for student in get_students():
                f.write(student.name + "\n")
        except Exception as e:
            print("Could not read from file {}".format(e))
        finally:
            f.close()

    @staticmethod
    def save_student(student):
        try:
            f = open(FileHelper.student_file, "a")
            f.write(student.name + "\n")
        except Exception as e:
            print("Could not read from file {}".format(e))
        finally:
            f.close()

    @staticmethod
    def read_students():
        try:
            f = open(FileHelper.student_file, "r")
            counter = 0
            for studentName in f.readlines():
                add_student(Student(studentName.replace("\n", ""), counter))
                counter += 1
            f.close()
        except Exception as e:
            print("Could not read from file {}".format(e))
