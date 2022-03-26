from App import db

#our model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    email = db.Column(db.String())
    password = db.Column(db.String(100))
 
 
    def __init__(self, username, password):
        self.username = username
        self.password = password