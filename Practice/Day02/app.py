# -----------------------------------------
# 📘 Flask Routing Examples
# -----------------------------------------
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# -------------------------------
# 1️⃣ Normal Routing
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

@app.route("/user/<name>")
def user(name):
    # Dynamic route with variable
    return f"Hello {name}"

@app.route("/user/admin")
def admin():
    return "Welcome Admin"

@app.route("/square/<int:number>")
def square(number):
    # Route with integer type conversion
    return f"Square = {number * number}"


# -------------------------------
# 2️⃣ Redirect + url_for
# -------------------------------
@app.route("/go-about")
def go_about():
    # Redirects to the 'about' route using url_for
    return redirect(url_for("about"))

@app.route("/test")
def test():
    # url_for generates the URL for 'user_profile'
    return url_for("user_profile")

@app.route("/search")
def search():
    keyword = request.args.get("q")
    return f"You searched for: {keyword}"


# -------------------------------
# 🚀 Run the Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
