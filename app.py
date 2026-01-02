from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        (name, email, password)
    )
    conn.commit()
    conn.close()

    return "Registration Successful"

app.run(debug=True)
