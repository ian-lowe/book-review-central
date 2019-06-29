import os

from flask import Flask, render_template, session, request
from flask_session import Session
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#initialize pw hashing
bcrypt = Bcrypt(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    username = request.form.get("username")
    password = request.form.get("password")

    user = db.execute("SELECT * FROM users WHERE username = :username",
    {"username": username}).fetchone()

    if user is None:
        return render_template("error.html", message="Account doesn't exist. Please create an account.")

    is_pass = bcrypt.check_password_hash(user.password, password)

    if is_pass == False:
        return render_template("error.html", message="Invalid password.")

    return render_template("search.html", username=username)

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/", methods=["POST"])
def register():
    username = request.form.get("username-reg").lower()
    password = bcrypt.generate_password_hash(request.form.get("password-reg")).decode('utf-8')

    if len(username) > 20:
        return render_template("index.html", message="Invalid username. Max length 20 characters")

    if len(password) < 6:
        return render_template("index.html", message="Invalid password. Minimum length 6 characters")

    username_checkdb = db.execute("SELECT * FROM users WHERE username = :username", {
        "username": username}).fetchone()

    if username_checkdb is None:
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username": username, "password": password})
        db.commit()
        return render_template("index.html", message="Success! Please log in.")

    else:
        return render_template("index.html", message="Username taken. Please choose another.")