from . import db
from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60))
    first_name = db.Column(db.String(150))
    folders = db.relationship('Folder', backref='user')

    def __repr__(self):
        return f"User('{self.email}')"


class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flashcards = db.relationship('Flashcard', backref='folder', lazy=True)

    def __repr__(self):
        return f"Folder('{self.title}', '{self.user.email}')"


class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    level = db.Column(db.Integer, default=0)
    next_review_date = db.Column(db.DateTime, default=datetime.utcnow())
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=False)

    def __repr__(self):
        return f"Flashcard('{self.question}', '{self.answer}', '{self.folder.title}')"




