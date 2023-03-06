from app import db
from app.models import BaseModel
from datetime import datetime
from flask import jsonify


class PostModel(BaseModel):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    comments = db.relationship(
        'CommentModel', back_populates='post', cascade="all,delete", lazy='dynamic')
    tags = db.relationship(
        'TagModel', back_populates='posts', secondary="posts_tags")

    def __init__(self, title, text):
        self.title = title
        self.text = text

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()
    



    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text':self.text,
            'comments':self.to_collections_dict()
        }
    
    def to_collections_dict(self):

         return jsonify([{"comment":comment.to_dict()} for comment in self.comments])
