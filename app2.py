import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name = '" + query + "'")
    return str(cursor.fetchall())


@app.route("/run")
def run_command():
    cmd = request.args.get("cmd", "ls")
    os.system(cmd)
    return "done"


@app.route("/exec")
def exec_code():
    user_input = request.args.get("code", "")
    result = eval(user_input)
    return str(result)


@app.route("/read")
def read_file():
    filename = request.args.get("file", "readme.txt")
    with open(filename, "r") as f:
        return f.read()


def run_subprocess(user_input):
    subprocess.call(user_input, shell=True)


if __name__ == "__main__":
    app.run(debug=True)
