from app import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    posts = db.Relationship(
        'PostModel', back_populates='tag', secondary="posts_tags")

    def __init__(self, name):
        self.name = name
