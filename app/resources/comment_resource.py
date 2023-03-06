from flask import Blueprint, request, jsonify
from app import db

from app.models import CommentModel
from app.models import PostModel

comment_bp = Blueprint("comment", __name__)


@comment_bp.route('/comments', methods=['POST'])
def write_comment():
    
    data = request.get_json()
    
    comment = CommentModel(
        data['text'],
        data['post_id'],
    )
    print(comment)
    
    comment.save_to_db()
   

    return comment.to_dict()


@comment_bp.route('/comments/<int:comment_id>',methods=['PUT'])
def update_comment(data, comment_id):

    comment = CommentModel.find_by_id(comment_id)

    if comment: 
        comment.text = data["text"]
    else:
        comment = CommentModel(id=comment_id, **data)
    
    return comment


@comment_bp.route('/comments/<int:comment_id>',methods=['DELETE'])
def delete_comment(comment_id):

    CommentModel.delete_from_db(comment_id)

    return {"Message":"Comment was deleted"}

#this works
@comment_bp.route('/comments/<int:comment_id>',methods=['GET'])
def get_comment_by_id(comment_id):

    return CommentModel.find_by_id(comment_id).to_dict()


#this works
@comment_bp.route('/comments',methods=['GET'])
def get_all_comments():

    comments =  CommentModel.find_all()

    comment_list = [{"comment":comment.to_dict()} for comment in comments]
    
    return jsonify(comment_list)

#this works
@comment_bp.route('/posts/<int:post_id>/comments',methods=['GET'])
def get_all_comments_for_a_post(post_id):

    comments = db.session.query(CommentModel).filter(CommentModel.post_id == post_id).all()

    comment_list = jsonify([{"comment":comment.to_dict()} for comment in comments])

    return comment_list


@comment_bp.route('/comments/comment_id', methods=['POST'])
def write_reply(data, comment_id):

    comment = CommentModel.find_by_id(comment_id)

    reply = CommentModel(**data)

    comment.comments.append(reply)
    





    



