from flask import Flask, render_template, redirect, url_for, request

from PyStudentManager.student import Student, get_student_list, add_student_to_list

from PyStudentManager.file_helper import FileHelper

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_forename = request.form.get("forename", "")
        new_lastname = request.form.get("lastname", "")

        new_student = Student(forename=new_forename,lastname=new_lastname, id=len(get_student_list()) + 1)
        add_student_to_list(new_student)
        FileHelper.save_student(new_student.__dict__)

        return redirect(url_for("students_page"))

    return render_template("index.html", students=get_student_list())


if __name__ == "__main__":
    FileHelper.read_students()
    app.run(debug=True)
