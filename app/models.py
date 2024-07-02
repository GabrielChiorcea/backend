from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique= True, nullable=False)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password,firstName, lastName, username):
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.username = username



class UniqueIdentify(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)

    def __init__(self, email, username):
        self.email = email,
        self.username = username
