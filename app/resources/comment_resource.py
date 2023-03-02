from flask import Blueprint, request
from app import db

from app.models import CommentModel
from app.models import PostModel

comment_bp = Blueprint("comment", __name__)


@comment_bp.route('/posts/<int:id>/comments', methods=['POST'])
def write_comment(data, post_id):
    post = PostModel.find_by_id(post_id)

    comment = CommentModel(**data)

    post.comments.append(comment)

    return comment


@comment_bp.route('/<ind:comment_id>',methods=['PUT'])
def update_comment(data, comment_id):

    comment = CommentModel.find_by_id(comment_id)

    if comment: 
        comment.text = data["text"]
    else:
        comment = CommentModel(id=comment_id, **data)
    
    return comment


@comment_bp.route('/<ind:comment_id>',methods=['DELETE'])
def delete_comment(comment_id):

    CommentModel.delete_from_db(comment_id)

    return {"Message":"Comment was deleted"}


@comment_bp.route('/<ind:comment_id>',methods=['GET'])
def get_comment_by_id(comment_id):

    return CommentModel.find_by_id(comment_id)



@comment_bp.route('/',methods=['GET'])
def get_all_comments():

    return CommentModel.find_all()


@comment_bp.route('/posts/<ind:post_id>/comments',methods=['GET'])
def get_all_comments_for_a_post(post_id):

    comments = db.session.query(CommentModel).filter(CommentModel.post_id == post_id).all()

    return comments


@comment_bp.route('/comments/comment_id', methods=['POST'])
def write_reply(data, comment_id):

    comment = CommentModel.find_by_id(comment_id)

    reply = CommentModel(**data)

    comment.comments.append(reply)





    



