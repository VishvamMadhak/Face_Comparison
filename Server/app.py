from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from cosinedist import test
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'face_comparison'

mysql = MySQL(app)


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
        response = jsonify( "Signup succesfull")
        response.status_code = 200
        return response



@app.route("/login", methods=["GET", "POST"])
def login():
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
            user_name = user[0]
            print(user_name)
            data = jsonify( message = "Login succesfull" , user_name = user_name)
            return data
        else:
            data = jsonify('Invalid credentials. Please try again.')
            return data

  


@app.route("/dashboard" , methods = ['POST'])
def dashboard():

    result = 0.0
    image1_path = ''
    image2_path = ''


    file1 = request.files['file1']
    file2 = request.files['file2']

    if 'file1' not in request.files or 'file2' not in request.files:
        return "No file found"
    
    if file1.filename == '' or file2.filename == '':
            return "No selected file"

    file1.save('uploads/' + file1.filename)
    file2.save('uploads/' + file2.filename)

    image1_path = 'uploads/' + file1.filename
    image2_path = 'uploads/' + file2.filename
    
    result = test(image1_path, image2_path)

    if result < 0.4:
        response = jsonify ("Both images are of the same person")
        return response
    else:
        response = jsonify("Identity is different")
        return response
    
        




if __name__ == '__main__':
    app.debug = True
    app.run()
