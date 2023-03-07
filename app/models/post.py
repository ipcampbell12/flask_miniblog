from app import db
from app.models import BaseModel
from datetime import datetime
from flask import jsonify, make_response


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
            'text':self.text
        }
    
    def get_all_comments(self):

        return [comment.to_dict() for comment in self.comments]

    def get_all_tags(self):

        return [tag.to_dict() for tag in self.tags]
    
    def to_collections_dict(self):
         return {
            'id': self.id,
            'title': self.title,
            'text':self.text,
            'comments':self.get_all_comments(),
            'tags':self.get_all_tags(),
            
        }
           

