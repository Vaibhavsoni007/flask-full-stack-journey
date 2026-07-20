# -----------------------------------------
# 📘 Flask Routing Examples (Organized)
# -----------------------------------------
from flask import Flask, redirect, url_for, request
import uuid   # Needed for UUID example

app = Flask(__name__)

# -------------------------------
# 1️⃣ Normal Routing (Static URLs)
# -------------------------------
@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/profile")
def user_profile():
    return "Profile Page"


# -------------------------------
# 2️⃣ Dynamic Routing (Variables in URL)
# -------------------------------
@app.route("/user/<name>")
def user(name):
    # <name> captures a string from the URL
    return f"Hello {name}"

@app.route("/square/<int:number>")
def square(number):
    # <int:number> ensures number is an integer
    return f"Square of {number} is {number * number}"

@app.route("/age/<int:age>")
def show_age(age):
    return f"Your age is {age}"


# -------------------------------
# 3️⃣ Path Converter Example
# -------------------------------
@app.route("/files/<path:subpath>")
def show_subpath(subpath):
    # <path:subpath> captures the entire path including slashes
    # Example: /files/images/profile/pic.png
    return f"Requested file path: {subpath}"


# -------------------------------
# 4️⃣ UUID Converter Example
# -------------------------------
@app.route("/item/<uuid:item_id>")
def get_item(item_id):
    # <uuid:item_id> ensures the value is a valid UUID
    # Example: /item/123e4567-e89b-12d3-a456-426614174000
    return f"Item ID: {item_id}"


# -------------------------------
# 5️⃣ Redirect + url_for
# -------------------------------
@app.route("/go-about")
def go_about():
    return redirect(url_for("about"))

@app.route("/test")
def test():
    return url_for("user_profile")


# -------------------------------
# 6️⃣ Routes with Request Parameters
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
    return "This page accepts only GET requests."

@app.route("/submit", methods=["POST"])
def submit():
    return "Form Submitted Successfully!"


# -------------------------------
# 🚀 Run the Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
