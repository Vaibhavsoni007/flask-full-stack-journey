# 📘 Day 01 - Flask Introduction & Routing

---

# 🎯 Goal of Day 01

By the end of today, we learned:

- What Flask is
- What a Framework is
- Why Flask is called Lightweight
- Flask vs Django
- Creating our first Flask application
- Routing
- Static Routes
- Dynamic Routes
- HTTP Request & Response
- HTTP Methods
- Debug Mode
- Development Server

---

# What is Flask?

Flask is a lightweight web framework written in Python.

It helps developers build web applications and APIs without writing everything from scratch.

Instead of creating your own web server, handling URLs, processing requests, and sending responses manually, Flask provides these features for you.

Think of Flask as a toolkit that gives you everything required to start building web applications.

---

# What is a Framework?

A framework is a collection of pre-written code that provides a structure for building applications.

Without a framework:

- We write everything ourselves.
- We manage requests manually.
- We build our own routing system.

With a framework:

- Routing is already available.
- Request handling is already implemented.
- Response handling is already implemented.
- Many common tasks become much easier.

Frameworks save time and encourage writing clean, organized code.

---

# Why is Flask Called Lightweight?

Flask is called lightweight because it only provides the essential features needed to build web applications.

It does **not** force developers to use:

- Database
- Authentication
- Forms
- ORM

You install only the features you need.

Example:

If your project requires MySQL, you install a MySQL library.

If your project requires authentication, you install an authentication package.

This makes Flask flexible and easy to customize.

---

# Flask vs Django

| Flask | Django |
|--------|---------|
| Lightweight | Full-featured Framework |
| Easy to Learn | Larger Learning Curve |
| Flexible | Opinionated Structure |
| Best for APIs and Small/Medium Projects | Best for Large Projects |
| Minimal by Default | Batteries Included |

---

# Our First Flask Program

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

# Explanation of Every Line

## Import Flask

```python
from flask import Flask
```

Imports the Flask class from the Flask package.

---

## Create Application

```python
app = Flask(__name__)
```

Creates the Flask application object.

`__name__` helps Flask locate resources such as templates and static files.

---

## Route Decorator

```python
@app.route("/")
```

Registers the URL `/`.

Whenever someone visits this URL, Flask calls the function immediately below it.

---

## Route Function

```python
def home():
```

A normal Python function.

Flask automatically calls it when the matching URL is requested.

---

## Return Statement

```python
return "Hello, Flask!"
```

The returned value becomes the HTTP response sent to the browser.

---

## Run the Server

```python
app.run(debug=True)
```

Starts Flask's development server.

`debug=True` enables automatic reloading and detailed error messages.

---

# Request–Response Cycle

```
Browser
    │
    │ HTTP Request
    ▼
Flask Server
    │
    ▼
Routing Table
    │
    ▼
Matching Function
    │
    ▼
Return Response
    │
    ▼
Browser
```

---

# What is a Route?

A route is a URL that is connected to a Python function.

Example:

```python
@app.route("/about")
def about():
    return "About Page"
```

When the browser requests `/about`, Flask executes `about()`.

---

# How Does Flask Know Which Function to Run?

Internally, Flask maintains a routing table.

Example:

| URL | Function |
|-----|----------|
| / | home() |
| /about | about() |
| /contact | contact() |

When a request arrives:

1. Flask checks the requested URL.
2. Searches the routing table.
3. Finds the matching function.
4. Executes that function.
5. Sends the returned value back to the browser.

---

# Static Routing

A static route always matches the same URL.

Example:

```python
@app.route("/about")
def about():
    return "About Page"
```

Valid URL:

```
/about
```

Invalid URLs:

```
/about1
/about/vaibhav
```

---

# Dynamic Routing

Dynamic routes capture values from the URL.

Example:

```python
@app.route("/user/<name>")
def user(name):
    return f"Welcome {name}"
```

Examples:

```
/user/vaibhav
```

Output:

```
Welcome vaibhav
```

```
/user/rahul
```

Output:

```
Welcome rahul
```

The same route handles multiple values.

---

# URL Converters

Flask automatically converts URL values into specific data types.

Example:

```python
@app.route("/square/<int:number>")
def square(number):
    return str(number * number)
```

Request:

```
/square/5
```

Output:

```
25
```

If a non-integer value is provided:

```
/square/hello
```

Flask returns **404 Not Found** because `"hello"` cannot be converted to an integer.

---

# HTTP Request

A request is sent by the client (browser) to the server asking for something.

Examples:

- Open Homepage
- Search Google
- View Profile
- View Products

---

# HTTP Response

A response is sent by the server back to the client.

The response may contain:

- HTML
- JSON
- Text
- Image
- Video
- PDF

---

# HTTP Methods

| Method | Purpose | Example |
|---------|----------|----------|
| GET | Read data | Open Homepage |
| POST | Send/Create data | Registration Form |
| PUT | Update existing data | Update Profile |
| DELETE | Delete data | Delete Account |

---

# GET Method

Used to retrieve data.

Example:

```python
@app.route("/home", methods=["GET"])
def home():
    return "Home Page"
```

---

# POST Method

Used to send data to the server.

Example:

```python
@app.route("/submit", methods=["POST"])
def submit():
    return "Submitted Successfully"
```

Trying to open this route directly in a browser using a GET request results in:

```
405 Method Not Allowed
```

because the route only accepts POST requests.

---

# Debug Mode

```python
app.run(debug=True)
```

Advantages:

- Automatically restarts the server after saving files.
- Displays detailed error messages.
- Speeds up development.

Never enable debug mode in production.

---

# Development Server

The server started using:

```python
app.run()
```

is intended only for development and testing.

It is **not** designed for production deployments.

---

# Common Beginner Mistakes

- Thinking Flask automatically runs every function.
- Forgetting the `@app.route()` decorator.
- Confusing GET and POST requests.
- Thinking the browser executes Python code.
- Returning unsupported data types instead of a valid response.
- Forgetting to activate the virtual environment before running the app.
- Leaving `debug=True` enabled in production.
- Assuming function names must match route names.

---

# Interview Questions

1. What is Flask?
2. What is a framework?
3. Why is Flask called lightweight?
4. Explain the request–response cycle.
5. What is routing?
6. What is the difference between static and dynamic routing?
7. What are URL converters in Flask?
8. Explain GET and POST methods.
9. What is the purpose of `debug=True`?
10. What is the difference between Flask and Django?
11. Why do we use `Flask(__name__)`?
12. Why do we use `if __name__ == "__main__"`?

---

# Key Takeaways

- Flask is a lightweight Python web framework.
- Every route maps a URL to a Python function.
- Flask uses a routing table to determine which function to execute.
- Browsers send HTTP requests; servers return HTTP responses.
- GET retrieves data, while POST sends data.
- Dynamic routes allow one function to handle multiple URLs.
- Debug mode improves development by enabling auto-reload and detailed error pages.
- The development server is for local development only.

---

# Practice Completed

- ✅ First Flask Application
- ✅ Multiple Static Routes
- ✅ Dynamic Routes
- ✅ Integer URL Converter
- ✅ GET Route
- ✅ POST Route
- ✅ Debug Mode
- ✅ Request–Response Cycle

---

# Assignment

1. Create a `/profile` route.
2. Create a `/skills` route.
3. Create a dynamic route `/city/<name>`.
4. Create `/cube/<int:number>` that returns the cube of the number.
5. Explain the Request–Response Cycle in your own words.