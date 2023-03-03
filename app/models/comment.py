from app import db
from datetime import datetime
from app.models import BaseModel


class CommentModel(BaseModel):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), unique=True, nullable=False)
    # parent_comment_id = db.Column(db.Integer, db.ForeignKey(
    #     'comments.id'), unique=True, nullable=False)
    # comments = db.relationship(
    #     'CommentModel', back_populates='comments', lazy="dynamic", cascade="all,delete")
    post = db.relationship('PostModel',back_populates='comments')

    def __init__(self, text):
        self.text = text

#to_dict() method