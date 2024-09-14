from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __init__(self,name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.is_active = True

=======
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

>>>>>>> novo-repo/main
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
<<<<<<< HEAD
            "name": self.name,
            "email": self.email,
            "is_active" : True
=======
            "id": self.id,
            "email": self.email,
>>>>>>> novo-repo/main
            # do not serialize the password, its a security breach
        }