from flask import Flask
from flask import render_template, request, redirect, url_for, session, flash
from datetime import datetime
import os
from dotenv import load_dotenv


app = Flask(__name__)
app.secret_key = os.urandom(24)
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
entries = []


class Entry:
    def __init__(self, content, happiness=None):
        self.content = content
        self.timestamp = datetime.now()
        self.happiness = happiness


mock_database = []


@app.route("/")
def index():
    return render_template("index.html", entries=entries)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_password = request.form.get("password")
        if user_password == PASSWORD:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Incorrect password. Please try again.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))


@app.route("/add_entry", methods=["POST"])
def add_entry():
    content = request.form.get("content")
    if content:
        entry = Entry(content=content)
        entries.append(entry)
    return redirect(url_for("index"))


@app.route("/add_entry_with_happiness", methods=["POST"])
def add_entry_with_happiness():
    content = request.form.get("content")
    happiness = request.form.get("happiness")

    # Instead of using a real database, store data in the mock database
    entry = Entry(content=content, happiness=happiness)
    mock_database.append(entry)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
