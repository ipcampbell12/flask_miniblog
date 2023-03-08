from app import db
from datetime import datetime
from app.models import BaseModel
from app.models import PostModel


class CommentModel(BaseModel):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), nullable=True)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey(
        'comments.id'), unique=False, nullable=True)
    parent_comment = db.relationship('CommentModel',remote_side=[id])
    replies = db.relationship(
        'CommentModel', back_populates='parent_comment' )
    post = db.relationship('PostModel',back_populates='comments')

    def __init__(self, text, post_id, parent_comment_id=None):
        self.text = text
        self.post_id = post_id
        self.parent_comment_id = parent_comment_id

    def to_dict(self):
        return {
            "id":self.id,
            "text":self.text,
            "post_id":self.post_id
        }
    
    def get_all_replies(self):

        return [reply.to_dict() for reply in self.replies]
    
    def to_collections_dict(self, post_id=0):
         return {
            "id":self.id,
            "text":self.text,
            "post_id":self.post_id,
            "post_title":PostModel.find_by_id(post_id).title,
            'replies':self.get_all_replies()
        }
    