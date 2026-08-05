from flask import Flask, render_template, request, redirect
from school import School
from student import Student
from teacher import Teacher
from classroom import Classroom
from timetable import Timetable

app = Flask(__name__, template_folder="template")
# Using the school name from your notes!
my_school = School("Hazara Public School", "123 Main St")

@app.route("/")
def home():
    return render_template("index.html")

# --- ADD ROUTES ---
@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name")
        s_id = request.form.get("id")
        grade = request.form.get("grade")
        my_school.add_student(Student(name, s_id, grade))
        return redirect("/")
    return render_template("add_student.html")

@app.route("/add_teacher", methods=["GET", "POST"])
def add_teacher():
    if request.method == "POST":
        name = request.form.get("name")
        spec = request.form.get("specialization") or request.form.get("subject")
        contact = request.form.get("contact") or request.form.get("id")
        my_school.add_teacher(Teacher(name, spec, contact))
        return redirect("/")
    return render_template("add_teacher.html")

@app.route("/add_classroom", methods=["GET", "POST"])
def add_classroom():
    if request.method == "POST":
        c_id = request.form.get("c_id") or request.form.get("id")
        cap = request.form.get("capacity")
        rtype = request.form.get("rtype") or request.form.get("room_type") or request.form.get("name")
        my_school.add_classroom(Classroom(c_id, cap, rtype))
        return redirect("/")
    return render_template("add_classroom.html")

@app.route("/add_timetable", methods=["GET", "POST"])
def add_timetable():
    if request.method == "POST":
        day = request.form.get("day") or request.form.get("classroom")
        time = request.form.get("time")
        subject = request.form.get("subject")
        my_school.add_timetable(Timetable(day, time, subject))
        return redirect("/")
    return render_template("add_timetable.html")

# --- VIEW DATA ROUTE ---
@app.route("/view_data")
def view_data():
    return render_template("view_data.html", school=my_school)

# --- DELETE DATA ROUTE ---
@app.route("/delete_data", methods=["GET", "POST"])
def delete_data():
    if request.method == "POST":
        s_id = request.form.get("student_id")
        if s_id:
            my_school.delete_student(s_id)
        return redirect("/view_data")
    return render_template("delete_data.html")

if __name__ == "__main__":
    app.run(debug=True)