from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_student(student_id):
    return Students.query.get(int(student_id))

class Students(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Students('{self.username}', '{self.email}')"
