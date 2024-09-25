from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.String(100), nullable=True)
    grade = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)

    def __str__(self):
        return f"{self.name}"