from app import db

posts_tags = db.Table(
    'post_tag',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('post_id', db.Integer(), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer(), db.ForeignKey('tags.id'))
)

comments_replies = db.Table(
    'comment_reply',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('comment_id', db.Integer(), db.ForeignKey('comments.id')),
    db.Column('reply_id', db.Integer(), db.ForeignKey('comments.id'))
)
