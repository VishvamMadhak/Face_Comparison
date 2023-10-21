from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
from flask_mysqldb import MySQL
from cosinedist import test
from flask_cors import CORS
import os
import secrets
import string

app = Flask(__name__)
secret_key = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(24))
app.secret_key = secret_key
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'face_comparison'

mysql = MySQL(app)


def get_user_folder(user_id):
    base_directory = 'uploads'
    user_folder = os.path.join(base_directory, str(user_id))

    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    return user_folder


@app.route('/')
def home():
    return render_template('home.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        cursor = mysql.connection.cursor()
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            response = jsonify(message="Missing fields in the request")
            response.status_code = 400
            return response

        cursor.execute(
            """ INSERT INTO users(email , name , password) VALUES (%s , %s , %s)""", (email, name, password))
        mysql.connection.commit()
        cursor.close()
        response = jsonify("Signup successful")
        response.status_code = 200
        return response


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ''
    if request.method == "POST" and 'email' in request.form and 'password' in request.form:
        email = request.form["email"]
        password = request.form["password"]

        if not email or not password:
            response = jsonify(message="Missing fields in the request")
            response.status_code = 400
            return response

        cursor = mysql.connection.cursor()
        cursor.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user_id'] = user[0]
            print("This is your user id:", session.get('user_id'))
            response = jsonify(session.get('user_id'))
            response = jsonify("Login successful")
            response.status_code = 205
            return response
        else:
            response = jsonify('Invalid credentials. Please try again.')
            return response


@app.route("/compare", methods=['POST'])
def compare():
    result = 0.0
    image1_path = ''
    image2_path = ''

    file1 = request.files['file1']
    file2 = request.files['file2']

    if 'file1' not in request.files or 'file2' not in request.files:
        return "No file found"

    if file1.filename == '' or file2.filename == '':
        return "No selected file"

    user_id = session.get('user_id')
    print("This is your user id in compare:", user_id)


    if user_id is None:
        response = jsonify("User not logged in")
        response.status_code = 401 
        return response
    
    user_folder = get_user_folder(user_id)

    file1.save(os.path.join(user_folder, file1.filename))
    file2.save(os.path.join(user_folder, file2.filename))

    image1_path = os.path.join(user_folder, file1.filename)
    image2_path = os.path.join(user_folder, file2.filename)

    result = test(image1_path, image2_path)
    print("This is the cosine distance between them:", result)

    if result < 0.4:
        response = jsonify("Both images are of the same person")
        return response
    else:
        response = jsonify("Identity is different")
        return response


if __name__ == '__main__':
    app.debug = True
    app.run()
