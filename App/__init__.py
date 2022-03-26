from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#create the object of Flask
app = Flask(__name__) 
 
# app.config['SECRET_KEY'] = 'hardsecretkey'
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 

db = SQLAlchemy(app)

#our model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(100), unique = True)
#     password = db.Column(db.String(100))
 
 
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#creating our routes
# @app.route('/')
# def index():
#     # user = User.query.all()
#     user = 1
#     return render_template('index.html')

# @app.route('/')
# def index():
#     # user = User.query.all()
#     # user = 1
#     return render_template('index.html')