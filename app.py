from flask import Flask, request, render_template, session, redirect, url_for
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Secret key used for sessions and CSRF protection
app.secret_key = os.urandom(32)

# Protect forms against CSRF attacks
csrf = CSRFProtect(app)

# Safer session cookie settings
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"


def get_db():
    connection = sqlite3.connect("users.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    db.commit()
    db.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if len(username) < 3:
            return "<h2>Username must be at least 3 characters.</h2>"

        if len(password) < 8:
            return "<h2>Password must be at least 8 characters.</h2>"

        hashed_password = generate_password_hash(password)

        db = get_db()

        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            db.commit()

        except sqlite3.IntegrityError:
            db.close()
            return "<h2>Username already exists.</h2>"

        db.close()

        return "<h2>Account created!</h2><a href='/login'>Login</a>"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        db.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        return "<h2>Invalid username or password.</h2>"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "welcome.html",
        username=session["username"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


@app.after_request
def add_security_headers(response):

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer"

    return response


if __name__ == "__main__":
    create_database()
    app.run(debug=False)