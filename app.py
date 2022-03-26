# from App import app, render_template
from flask import Flask, render_template, flash, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(100), unique = True)
#     password = db.Column(db.String(100))
 
 
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

# import routes
# from Models.User import User

# @app.route("/")
# def index():
#     user = User.query.all()
#     return user
@app.route('/')
def index():
    # users = User.query.all()
    # # user = 1
    # for user in users:
    #     return user
    return render_template('index.html')
#run flask app
if __name__ == "__main__":
    app.run(debug=True)