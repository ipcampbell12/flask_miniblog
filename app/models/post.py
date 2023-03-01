from app import db
from datetime import datetime


class PostModel(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    comments = db.Relationship(
        'CommentModel', back_populates='post', lazy="dynamic", cascade="all,celete")
    tags = db.Relationship(
        'TagModel', back_pouplates='post', secondary="posts_tags")
