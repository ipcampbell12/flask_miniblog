from app import db

posts_tags = db.Table(
    'posts_tags',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


