from app import db
from datetime import datetime


class CommentModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
