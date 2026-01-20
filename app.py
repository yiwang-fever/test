from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def user():
    name = request.args.get("name")
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '%s'" % name)
    return "ok"
