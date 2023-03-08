from app.models import BaseModel
from app import db


class TagModel(BaseModel):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    posts = db.relationship('PostModel', back_populates='tags', secondary="posts_tags")

    def __init__(self, name):
        self.name = name

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name
        }
    
 