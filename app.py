from flask import Flask, request, render_template
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect
app = Flask(__name__)

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="Dhurendhar",
    user="postgres",
    password="aswq"
)

cursor = conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- SIGNUP ---------------- #

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    phone = request.form["phone"]
    email = request.form["email"]

    hashed_password = generate_password_hash(password)

    query = """
    INSERT INTO UserDetails (Name, UserName, PasswordHash, PhoneNumber, EmailID)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, username, hashed_password, phone, email))
    conn.commit()

    return "Signup Successful! You can now login."

# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    query = "SELECT Name, PasswordHash FROM UserDetails WHERE UserName = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        name = user[0]
        stored_hash = user[1]

        if check_password_hash(stored_hash, password):
            return f"Hey {name}, how are you? 😊"
        else:
            return "wrong password  please remember and try aagain"
    else:
        return "No account buddy, first create it."

# --------------------------------------- #

if __name__ == "__main__":
    app.run(debug=True)