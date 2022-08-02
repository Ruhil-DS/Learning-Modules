from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)

data = open("data.csv", "r")

# Reading the first line of headings
a = data.readline()

# Creating empty lists to store data
student_id = []
course_id = []
marks = []

# While loop to add data to respective lists
while a != "":
    a = data.readline()
    if a != "":
        l = a.split(",")
        student_id.append(int(l[0]))
        course_id.append(int(l[1]))
        marks.append(int(l[2]))

data.close()


@app.route("/", methods=["GET", "POST"])
def main_code():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':

        try:
            choice = request.form["ID"]
        except KeyError:
            choice = None

        try:
            choice_value = int(request.form["id_value"])
        except:
            choice_value = None

        if choice == "student_id":
            rows_stu = []
            tot_marks_stu = 0

            for i in range(len(student_id)):
                if student_id[i] == choice_value:  # CHANGE THIS TO STU_ID
                    rows_stu.append((student_id[i], course_id[i], marks[i]))
                    tot_marks_stu += marks[i]
            if len(rows_stu)==0:
                return render_template("error.html")

            return render_template("stu_data.html", rows_stu=rows_stu, tot_marks_stu=tot_marks_stu)

        elif choice == "course_id":

            rows_crs = []
            tot_marks_crs = 0

            for i in range(len(course_id)):
                if course_id[i] == choice_value:
                    rows_crs.append(marks[i])
                    tot_marks_crs += marks[i]

            if len(rows_crs) == 0:
                return render_template("error.html")

            max_marks = max(rows_crs)
            avg_marks = tot_marks_crs / (len(rows_crs))

            plt.hist(rows_crs)
            plt.savefig(r"static/histogram.png")

            return render_template("crs_data.html", max_marks=max_marks, avg_marks=avg_marks)
        else:
            return render_template("error.html")
app.run()