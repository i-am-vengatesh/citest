#app.py
from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/submit", methods=["POST"])
def submit():
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "branch": request.form["branch"],
        "key": request.form["key"]
    }

    json_data = json.dumps(user_data)

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (data) VALUES (?)", (json_data,))
    conn.commit()
    conn.close()

    return "Data stored successfully!"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

