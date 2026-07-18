from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Home Page"


@app.route("/about")
def about():
    return "This is About Page"


@app.route("/contact")
def contact():
    return "Contact Us"

@app.route("/services")
def services():
    return "our Services"

@app.route("/courses")
def courses():
    return "python Courses"

@app.route("/flask")
def flask():
    return "learn Flask"

@app.route("/github")
def github():
    return "github page"

@app.route("/hello", methods=["GET"])
def hello():
    return "This page accepts only GET requests."

@app.route("/submit", methods=["POST"])
def submit():
    return "Form Submitted Successfully!"

@app.route("/age/<int:age>")
def show_age(age):
    return f"Your age is {age}"

@app.route("/user/<name>")
def user(name):
    return f"Welcome {name}"

@app.route("/square/<int:number>")
def square(number):
    return f"Square of {number} is {number * number}"

if __name__ == "__main__":
    app.run(debug=True)