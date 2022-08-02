from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Initialising the DB using SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///week7_database.sqlite3'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class STUDENT(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    # c = db.relationship('COURSE', secondary='enrollments')


class COURSE(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)


class ENROLLMENT(db.Model):
    __tablename__ = "enrollments"
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey(STUDENT.student_id), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey(COURSE.course_id), nullable=False)


db.session.commit()


# Till now, we have set up the model. Now comes the turn of our app


@app.route("/", methods=["GET", "POST"])
def home():
    students = STUDENT.query.all()
    if students:
        return render_template("home.html", flag=True, students=students)
    else:
        return render_template("home.html", flag=False)


@app.route("/student/create/", methods=["GET", "POST"])
def create_stu():
    if request.method == "GET":
        return render_template("add_student.html")

    elif request.method == "POST":
        try:
            roll = request.form['roll']
            fname = request.form['f_name']
            lname = request.form['l_name']

            record = STUDENT(roll_number=roll, first_name=fname, last_name=lname)
            try:
                db.session.add(record)
                db.session.commit()
                status = True
            except:
                db.session.rollback()
                status = False
                return render_template("error_stu.html")


            finally:
                if status:
                    return redirect("/")

        except:
            return render_template("error_stu.html")
        students = STUDENT.query.all()
        return render_template("home.html", students=students)


@app.route("/student/<int:student_id>/update/", methods=["GET", "POST"])
def update_stu(student_id):
    if request.method == "GET":
        current_student = STUDENT.query.filter_by(student_id=student_id).first()
        current_courses = COURSE.query.all()

        return render_template("update_stu.html", current_roll=current_student.roll_number,
                               current_f_name=current_student.first_name, current_l_name=current_student.last_name,
                               current_courses=current_courses, student_id=student_id)
    elif request.method == "POST":
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        course_choice = request.form['course']

        current_record = STUDENT.query.filter_by(student_id=student_id).first()

        current_record.first_name = f_name
        current_record.last_name = l_name
        enroll_record = ENROLLMENT(estudent_id=student_id, ecourse_id=course_choice)
        db.session.add(enroll_record)
        db.session.commit()

        return redirect("/")


@app.route("/student/<int:student_id>/delete/", methods=["GET"])
def delete_stu(student_id):
    enroll_records = ENROLLMENT.query.filter_by(estudent_id=student_id).all()
    for enroll_record in enroll_records:
        db.session.delete(enroll_record)
    db.session.commit()
    stu_record = STUDENT.query.filter_by(student_id=student_id).first()
    db.session.delete(stu_record)
    db.session.commit()

    return redirect("/")


@app.route("/student/<int:student_id>/", methods=["GET"])
def view_stu(student_id):
    enroll_records = ENROLLMENT.query.filter_by(estudent_id=student_id).all()

    courses = []

    for enroll in enroll_records:
        course_record = COURSE.query.filter_by(course_id=enroll.ecourse_id).first()
        courses.append(course_record)

    student = STUDENT.query.filter_by(student_id=student_id).first()
    return render_template('personal_details.html', student=student, courses=courses)


@app.route("/student/<int:student_id>/withdraw/<int:course_id>")
def withdraw_course(student_id, course_id):
    enroll_records_stu = ENROLLMENT.query.filter_by(estudent_id=student_id).all()
    enroll_records = []
    for i in enroll_records_stu:
        if i.ecourse_id == course_id:
            enroll_records.append(i)

    for enroll in enroll_records:
        db.session.delete(enroll)
        db.session.commit()
    return redirect("/")


@app.route("/courses/", methods=["GET", "POST"])
def course_home():
    courses = COURSE.query.all()
    if courses:
        return render_template("courses_home.html", flag=True, courses=courses)
    else:
        return render_template("courses_home.html", flag=False)


@app.route("/course/create/", methods=["GET", "POST"])
def create_course():
    if request.method == "GET":
        return render_template("add_course.html")

    elif request.method == "POST":
        try:
            code = request.form['code']
            c_name = request.form['c_name']
            desc = request.form['desc']

            record = COURSE(course_code=code, course_name=c_name, course_description=desc)

            try:
                db.session.add(record)
                db.session.commit()
                status = True
            except:
                db.session.rollback()
                db.session.commit()
                status = False
                return render_template("error_course.html")

            finally:
                if status:
                    return redirect("/courses")

        except:
            return render_template("error_course.html")
        courses = COURSE.query.all()
        return render_template("courses_home.html", courses=courses)


@app.route("/course/<int:course_id>/update/", methods=["GET", "POST"])
def update_course(course_id):
    if request.method == "GET":
        current_course = COURSE.query.filter_by(course_id=course_id).first()

        return render_template("update_c.html", course_id=course_id, current_code=current_course.course_code,
                               current_c_name=current_course.course_name,
                               current_desc=current_course.course_description)
    elif request.method == "POST":
        new_cname = request.form['c_name']
        new_desc = request.form['desc']
        record = COURSE.query.filter_by(course_id=course_id).first()
        record.course_name = new_cname
        record.course_description = new_desc
        db.session.commit()
        return redirect("/courses/")


@app.route("/course/<int:course_id>/delete/", methods=["GET"])
def delete_c(course_id):
    enroll_records = ENROLLMENT.query.filter_by(ecourse_id=course_id).all()
    for enroll_record in enroll_records:
        db.session.delete(enroll_record)
    db.session.commit()
    c_record = COURSE.query.filter_by(course_id=course_id).first()
    db.session.delete(c_record)
    db.session.commit()

    return redirect("/")


@app.route("/course/<int:course_id>/", methods=["GET"])
def view_c(course_id):
    c_record = COURSE.query.filter_by(course_id=course_id).first()
    enroll_records = ENROLLMENT.query.filter_by(ecourse_id=course_id).all()

    students = []

    for enroll in enroll_records:
        stu_record = STUDENT.query.filter_by(student_id=enroll.estudent_id).first()
        students.append(stu_record)

    course = COURSE.query.filter_by(course_id=course_id).first()
    return render_template('course_details.html', course=course, students=students)


app.run(port=5004)
