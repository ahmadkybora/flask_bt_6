from Models.User import User
from App import app

@app.route("/")
def index():
    user = User.query.all()
    return user
