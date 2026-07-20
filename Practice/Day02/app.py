# -----------------------------------------
# 📘 Flask Routing Examples (Organized)
# -----------------------------------------
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# -------------------------------
# 1️⃣ Normal Routing (Static URLs)
# -------------------------------
@app.route("/")
def home():
    # Simple static route
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/profile")
def user_profile():
    return "Profile Page"

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
# 2️⃣ Dynamic Routing (Variables in URL)
# -------------------------------
@app.route("/user/<name>")
def user(name):
    # <name> captures a string from the URL
    return f"Hello {name}"

@app.route("/user/admin")
def admin():
    return "Welcome Admin"

@app.route("/square/<int:number>")
def square(number):
    # <int:number> ensures number is an integer
    return f"Square of {number} is {number * number}"

@app.route("/age/<int:age>")
def show_age(age):
    # <int:age> ensures age is an integer
    return f"Your age is {age}"


# -------------------------------
# 3️⃣ Redirect + url_for
# -------------------------------
@app.route("/go-about")
def go_about():
    # Redirects to the 'about' route using url_for
    return redirect(url_for("about"))

@app.route("/test")
def test():
    # url_for generates the URL for 'user_profile'
    return url_for("user_profile")


# -------------------------------
# 4️⃣ Routes with Request Parameters
# -------------------------------
@app.route("/search", methods=["GET"])
def search():
    # Example: /search?q=python
    keyword = request.args.get("q")
    return f"You searched for: {keyword}"

@app.route("/greet", methods=["GET"])
def greet():
    # Example: /greet?name=Vaibhav
    name = request.args.get("name")
    return f"Hello {name}"

@app.route("/student", methods=["GET"])
def student():
    # Example: /student?name=Shad&age=22
    name = request.args.get("name")
    age = request.args.get("age")
    return f"Student: {name}, Age: {age}"

@app.route("/hello", methods=["GET"])
def hello():
    # Only accepts GET requests
    return "This page accepts only GET requests."

@app.route("/submit", methods=["POST"])
def submit():
    # Only accepts POST requests
    return "Form Submitted Successfully!"


# -------------------------------
# 🚀 Run the Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
