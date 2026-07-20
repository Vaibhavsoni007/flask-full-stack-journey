# -----------------------------------------
# 📘 Flask Routing Examples
# -----------------------------------------
from flask import Flask

app = Flask(__name__)

# -------------------------------
# 1️⃣ Normal Routing (Static URLs)
# -------------------------------
@app.route("/")
def home():
    # Simple static route
    return "Welcome to Home Page"

@app.route("/about")
def about():
    return "This is About Page"

@app.route("/contact")
def contact():
    return "Contact Us"

@app.route("/services")
def services():
    return "Our Services"

@app.route("/courses")
def courses():
    return "Python Courses"

@app.route("/flask")
def flask_course():
    return "Learn Flask"

@app.route("/github")
def github():
    return "GitHub Page"


# -------------------------------
# 2️⃣ Routing with HTTP Methods
# -------------------------------
@app.route("/hello", methods=["GET"])
def hello():
    # This route only accepts GET requests
    return "This page accepts only GET requests."

@app.route("/submit", methods=["POST"])
def submit():
    # This route only accepts POST requests
    return "Form Submitted Successfully!"


# -------------------------------
# 3️⃣ Dynamic Routing (Variables in URL)
# -------------------------------
@app.route("/age/<int:age>")
def show_age(age):
    # <int:age> ensures age is an integer
    return f"Your age is {age}"

@app.route("/user/<name>")
def user(name):
    # <name> captures a string from the URL
    return f"Welcome {name}"

@app.route("/square/<int:number>")
def square(number):
    # <int:number> ensures number is an integer
    return f"Square of {number} is {number * number}"


# -------------------------------
# 🚀 Run the Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
