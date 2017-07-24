students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt" , "a")
        f.write(student + "\n")
    except Exception as e:
        print("Could not read from file {}".format(e))
    finally:
        f.close()


def read_file():
    try:
        f = open("students.txt" , "r")
        counter = 0
        for student in f.readlines():
            add_student(student, counter)
            counter += 1
        f.close()
    except Exception as e:
        print("Could not read from file {}".format(e))


read_file()
print("Current students are: {0}".format(students))

while input("Do you want to add a student? (y/n)") == "y":
    add_student(input("Student name:"), input("Student id:"))

for i in range(0, students.__len__()):
    save_file(students[i]["name"])

print("Current students are: {0}".format(students))
