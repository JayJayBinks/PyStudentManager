from flask import Flask, render_template, redirect, url_for, request

from PyStudentManager.student import Student, get_students, add_student

from PyStudentManager.file_helper import FileHelper

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")

        new_student = Student(name=new_student_name, student_id=new_student_id)
        add_student(new_student)
        FileHelper.save_student(new_student)

        return redirect(url_for("students_page"))

    return render_template("index.html", students=get_students())


if __name__ == "__main__":
    FileHelper.read_students()
    app.run(debug=True)
