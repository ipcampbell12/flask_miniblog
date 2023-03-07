from app import db
from datetime import datetime
from app.models import BaseModel


class CommentModel(BaseModel):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), nullable=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey(
        'comments.id'), unique=False, nullable=True)
    parent_comment = db.relationship('CommentModel',remote_side=[id])
    replies = db.relationship(
        'CommentModel', back_populates='parent_comment', )
    post = db.relationship('PostModel',back_populates='comments',cascade="all,delete")

    def __init__(self, text, post_id):
        self.text = text
        self.post_id = post_id

    def to_dict(self):
        return {
            "id":self.id,
            "text":self.text,
            "post_id":self.post_id
        }
    
    def get_all_replies(self):

        return [reply.to_dict() for reply in self.replies]
    
    def to_collections_dict(self):
         return {
             "id":self.id,
            "text":self.text,
            "post_id":self.post_id,
            'replies':self.get_all_replies()
        }