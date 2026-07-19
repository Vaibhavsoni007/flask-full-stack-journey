# 📘 Day 02 - Advanced Routing, URL Building & Query Parameters

---

# 🎯 Goal of Day 02

Today we learned how Flask performs routing internally, how URL converters work, how to generate URLs using `url_for()`, how redirects work, and how to use query parameters to receive additional information from the client.

---

# Topics Covered

- Route Matching
- Routing Map
- Route Priority
- URL Converters
- `url_for()`
- `redirect()`
- HTTP 302 Redirect
- Query Parameters
- Dynamic Routes vs Query Parameters
- Real-World Use Cases

---

# Revision of Day 01

Before learning new concepts, we revised:

- Flask Framework
- First Flask Application
- Request–Response Cycle
- Routing
- Static Routes
- Dynamic Routes
- HTTP Methods

---

# How Flask Finds the Correct Route

When the Flask application starts, it registers all routes and creates a routing map.

Example:

```python
@app.route("/")
def home():
    return "Home"

@app.route("/about")
def about():
    return "About"

@app.route("/contact")
def contact():
    return "Contact"
```

Internally, Flask maintains a routing map similar to:

| URL | Function |
|------|----------|
| / | home() |
| /about | about() |
| /contact | contact() |

When a request arrives:

```
Browser
    │
GET /contact
    │
    ▼
Routing Map
    │
Find Matching Route
    │
    ▼
contact()
    │
    ▼
Response Sent Back
```

Only the matching function is executed.

---

# What Happens If No Route Exists?

Example:

```
/abc
```

Flask searches its routing map.

No matching route is found.

Result:

```
404 Not Found
```

This means the requested resource does not exist.

---

# Route Priority

Example:

```python
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/user/admin")
def admin():
    return "Welcome Admin"
```

Visiting:

```
/user/admin
```

Output:

```
Welcome Admin
```

because Flask chooses the more specific route.

Visiting:

```
/user/vaibhav
```

Output:

```
Hello vaibhav
```

---

# URL Converters

URL converters automatically convert URL values into Python data types before passing them to the function.

---

## String Converter

```python
@app.route("/user/<string:name>")
```

Example:

```
/user/vaibhav
```

Output:

```
Welcome vaibhav
```

The `string` converter is the default converter.

---

## Integer Converter

```python
@app.route("/age/<int:age>")
```

Example:

```
/age/25
```

Output:

```
Age: 25
```

Example:

```
/age/hello
```

Output:

```
404 Not Found
```

Reason:

Flask cannot convert `"hello"` into an integer, so the route does not match and the function is never executed.

---

## Float Converter

```python
@app.route("/price/<float:amount>")
```

Example:

```
/price/199.99
```

Output:

```
199.99
```

---

## Path Converter

```python
@app.route("/file/<path:filepath>")
```

Example:

```
/file/images/profile/photo.png
```

Output:

```
images/profile/photo.png
```

Unlike the string converter, the path converter allows `/` inside the value.

---

## UUID Converter

Used for unique identifiers.

Example:

```python
@app.route("/order/<uuid:order_id>")
```

Mostly used in large applications and APIs.

---

# Built-in URL Converters

| Converter | Python Type | Example |
|-----------|-------------|---------|
| string | str | `/user/vaibhav` |
| int | int | `/age/21` |
| float | float | `/price/99.99` |
| path | str | `/file/images/photo.png` |
| uuid | UUID | `/order/<uuid>` |

---

# url_for()

## What is url_for()?

`url_for()` generates the correct URL for a given Flask view function.

Instead of hardcoding URLs:

```html
<a href="/about">
```

use:

```python
url_for("about")
```

---

## Example

```python
@app.route("/profile")
def user_profile():
    return "Profile"

@app.route("/test")
def test():
    return url_for("user_profile")
```

Output:

```
/profile
```

---

# Why use url_for()?

Advantages:

- Avoids hardcoded URLs.
- Easier to maintain.
- If a route changes, only the route definition needs updating.
- Widely used in templates and redirects.

---

# redirect()

`redirect()` sends the client to another route.

Example:

```python
return redirect(url_for("about"))
```

---

## Redirect Flow

```
Browser

GET /go-about

↓

Flask

↓

302 Redirect

Location: /about

↓

Browser sends another request

GET /about

↓

About Page
```

A redirect causes the browser to make a new request.

---

# Query Parameters

Query parameters are additional data sent after `?` in a URL.

Example:

```
/search?q=python
```

Here:

- Route → `/search`
- Query Parameter → `q`
- Value → `python`

---

# Reading Query Parameters

```python
from flask import request

@app.route("/search")
def search():
    keyword = request.args.get("q")
    return f"You searched for: {keyword}"
```

Example:

```
/search?q=flask
```

Output:

```
You searched for: flask
```

---

# Multiple Query Parameters

Example:

```
/student?name=Rahul&age=21
```

```python
@app.route("/student")
def student():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"{name} - {age}"
```

Output:

```
Rahul - 21
```

---

# Dynamic Route vs Query Parameter

| Dynamic Route | Query Parameter |
|--------------|-----------------|
| `/user/vaibhav` | `/user?name=vaibhav` |
| Part of URL path | Additional information after `?` |
| Used to identify a specific resource | Used for search, filtering, sorting, pagination |

---

# Real-World Uses

Dynamic Routes:

- Student Details
- Product Details
- Blog Posts
- User Profiles

Query Parameters:

- Search
- Product Filters
- Sorting
- Pagination
- Category Selection

---

# Common Beginner Mistakes

- Thinking all routes execute for every request.
- Forgetting that `url_for()` uses the function name, not the URL.
- Hardcoding URLs instead of using `url_for()`.
- Confusing dynamic routes with query parameters.
- Assuming query parameters are required.
- Forgetting to import `request`.
- Confusing `404 Not Found` with `405 Method Not Allowed`.

---

# Interview Questions

1. How does Flask find the correct route?
2. What is the routing map?
3. What is route priority?
4. Explain all URL converters.
5. What is the difference between `string` and `path` converters?
6. What does `url_for()` do?
7. Why should we avoid hardcoded URLs?
8. What is `redirect()`?
9. Why does a redirect create another request?
10. What are query parameters?
11. Difference between dynamic routes and query parameters?
12. When should you use each?

---

# Key Takeaways

- Flask registers routes when the application starts.
- Only the matching route function is executed.
- URL converters validate and convert values before entering the function.
- `url_for()` generates URLs using function names.
- `redirect()` instructs the browser to make a new request.
- Query parameters provide additional request data for search and filtering.
- Dynamic routes identify specific resources, while query parameters modify or filter results.

---

# Practice Completed

- ✅ Route Matching
- ✅ Route Priority
- ✅ URL Converters
- ✅ `url_for()`
- ✅ `redirect()`
- ✅ Query Parameters
- ✅ Dynamic Routes vs Query Parameters