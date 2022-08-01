from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

mysql = MySQL()

# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# # app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'python_flask'
# app.config['MYSQL_DATABASE_HOST'] = 'mysql'
# # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_PORT'] = 3306

app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PWD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DB_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_DATABASE_PORT'] = int(os.environ.get('DB_PORT'))
mysql.init_app(app)


@app.route('/')
def render_login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    cursor = mysql.get_db().cursor()
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    cursor.execute("SELECT COUNT(*) FROM users WHERE user_name=%s and password=%s", (user_name, password))
    user_count = cursor.fetchall()[0][0]
    if user_count == 0:
        return 'Login Failed'
    else:
        return 'Login Successful'


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
