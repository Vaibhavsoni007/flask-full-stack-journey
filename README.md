# 🚀 Flask Development Journey

A complete learning journey of Flask Web Development.

This repository documents my journey of learning Flask from beginner to intermediate level, including:

- Flask fundamentals
- Routing
- HTML/CSS/JavaScript integration
- Database integration with MySQL
- Authentication
- REST APIs
- Project development
- Deployment basics

The goal of this repository is to build a strong foundation in backend development using Python Flask.

---

# 🎯 Learning Goal

By completing this journey, I aim to understand:

- How Flask works internally
- How backend applications are structured
- How frontend communicates with backend
- How databases connect with web applications
- How to build real-world Flask projects

---

# 🛠️ Technologies Used

## Backend

- Python
- Flask

## Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

## Database

- MySQL

## Tools

- VS Code
- Git
- GitHub
- Postman

---

# 📚 15 Days Flask Roadmap

| Day | Topic | Status |
|-----|-------|--------|
| Day 01 | Flask Introduction, Routing, Request-Response Cycle | ✅ Completed |
| Day 02 | Advanced Routing, HTTP Methods | ⏳ Pending |
| Day 03 | Flask Templates and Jinja2 | ⏳ Pending |
| Day 04 | Integrating HTML, CSS, JavaScript | ⏳ Pending |
| Day 05 | Forms and User Input Handling | ⏳ Pending |
| Day 06 | Redirects, Sessions, Flash Messages | ⏳ Pending |
| Day 07 | Connecting MySQL with Flask | ⏳ Pending |
| Day 08 | CRUD Operations with Database | ⏳ Pending |
| Day 09 | Authentication System | ⏳ Pending |
| Day 10 | File Upload Handling | ⏳ Pending |
| Day 11 | Professional Flask Project Structure | ⏳ Pending |
| Day 12 | REST APIs with Flask | ⏳ Pending |
| Day 13 | Advanced Authentication + Database | ⏳ Pending |
| Day 14 | Deployment Basics | ⏳ Pending |
| Day 15 | Final Mini Project | ⏳ Pending |

---

# 📂 Repository Structure

```
Flask-Development-Journey
│
├── README.md
│
├── Notes
│   │
│   ├── Day01
│   │   └── notes.md
│   │
│   ├── Day02
│   │   └── notes.md
│   │
│   └── ...
│
├── Practice
│   │
│   ├── Day01
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── README.md
│   │
│   └── ...
│
├── Mini Projects
│
├── Major Projects
│
└── Resources
    │
    ├── Commands.md
    ├── CheatSheet.md
    └── InterviewQuestions.md
```

---

# 📖 Day 01 - Flask Introduction & Routing

## Topics Covered

- Introduction to Flask
- What is a Framework
- Why Flask is Lightweight
- Flask vs Django
- Creating First Flask Application
- Flask Application Object
- Routing
- Static Routes
- Dynamic Routes
- URL Parameters
- HTTP Request and Response
- HTTP Methods
- Debug Mode
- Development Server

---

# 💻 Day 01 Practice

Created my first Flask application with:

### Static Routes

Examples:

```
/
/about
/contact
```

### Dynamic Routes

Examples:

```
/user/<name>

/square/<int:number>
```

---

# 🔄 Request Response Cycle

```
Browser
   |
   | HTTP Request
   ↓
Flask Server
   |
   ↓
Routing Table
   |
   ↓
Python Function
   |
   ↓
HTTP Response
   |
   ↓
Browser
```

---

# 🧠 Important Concepts Learned

### Routing

Mapping a URL to a Python function.

Example:

```python
@app.route("/about")
def about():
    return "About Page"
```

---

### Dynamic Routing

Creating flexible URLs.

Example:

```python
@app.route("/user/<name>")
def user(name):
    return f"Welcome {name}"
```

---

### HTTP Methods

| Method | Purpose |
|--------|---------|
| GET | Retrieve Data |
| POST | Send Data |
| PUT | Update Data |
| DELETE | Remove Data |

---

# 📒 Notes

Detailed notes for every day are available here:

```
Notes/Day01/notes.md
```

---

# 🏗️ Future Projects

After completing Flask fundamentals, I will build:

## Mini Projects

- Portfolio Website
- To-Do Application
- Notes Application
- Student Registration System
- Expense Tracker

## Major Projects

- Blog Platform
- E-Commerce Website
- Job Portal
- Hospital Management System
- Learning Management System
- CRM Application

---

# 📈 Progress

Current Progress:

```
Flask Fundamentals
████░░░░░░░░░░░░ 10%
```

---

# 🤝 Learning Approach

Every day follows this workflow:

```
Learn Concept
      ↓
Understand Theory
      ↓
Write Code
      ↓
Practice
      ↓
Create Notes
      ↓
Push to GitHub
```

---

# ⭐ Repository Purpose

This repository is not just a collection of code.

It represents my complete Flask development journey, including:

- Concepts learned
- Practical implementations
- Notes
- Projects
- Mistakes and improvements

---

# 👨‍💻 Author

Vaibhav

Learning Backend Development with Python Flask 🚀