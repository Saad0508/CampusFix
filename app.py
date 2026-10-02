from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "campusfix-dev-key"

complaints = [
    {
        "id": "CF-2026-0148",
        "title": "Projector not working",
        "location": "Lecture Hall 2",
        "status": "Assigned"
    }
]

@app.route("/")
def login():
    if session.get("logged_in"):
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def do_login():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    # Demo credentials for the Assignment 3 prototype
    if email == "student@campusfix.com" and password == "123456":
        session["logged_in"] = True
        return redirect(url_for("dashboard"))

    return render_template(
        "login.html",
        error="Invalid email or password. Try student@campusfix.com / 123456."
    )

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html", complaints=complaints)

@app.route("/complaint", methods=["POST"])
def add_complaint():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    title = request.form.get("title", "").strip()
    location = request.form.get("location", "").strip()
    priority = request.form.get("priority", "").strip()

    if title and location:
        complaint_id = f"CF-2026-{len(complaints) + 149:04d}"
        complaints.append({
            "id": complaint_id,
            "title": title,
            "location": location,
            "status": "Submitted"
        })

    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
