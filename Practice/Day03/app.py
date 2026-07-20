from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# passing variable to the template
@app.route("/home1")
def home1():
    return render_template("home.html", name="Vaibhav")

@app.route("/student")
def student():
    marks = 89
    return render_template(
        "student.html",
        name="Vaibhav",
        age=21,
        city="Jaipur"
    )

# jinja2 loops
@app.route("/students")
def students():
    marks = 90

    student_list = [
        "Vaibhav",
        "Rahul",
        "Aman",
        "Rohit",
        "Karan"
    ]

    return render_template(
        "student.html",
        students=student_list
    )

# jinja2 basic if else
@app.route("/home2")
def home2():
    marks = 82
    return render_template("home.html", marks=marks)

@app.route("/result")
def result():
    marks = 68
    return render_template("result.html", marks=marks)

# template inheritance
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)