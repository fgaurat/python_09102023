from flask import Flask,render_template
from UserDAO import UserDAO
app = Flask(__name__)

@app.route("/")
def hello_world():
    dao = UserDAO('users_db.db')
    users = list(dao.findAll())
    return render_template('hello.html',users=users)