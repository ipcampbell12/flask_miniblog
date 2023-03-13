from flask import Blueprint, request, jsonify
from app import db
from flask_smorest import abort
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
   

    return comment.to_collections_dict()


@comment_bp.route('/comments/<int:comment_id>',methods=['PUT'])
def update_comment(comment_id):

    data = request.get_json()
    comment = CommentModel.find_by_id(comment_id)

    if comment: 
        comment.text = data["text"]
    else:
        comment = CommentModel(id=comment_id, **data)
    
    comment.save_to_db()
    
    return comment.to_collections_dict()


@comment_bp.route('/comments/<int:comment_id>',methods=['DELETE'])
def delete_comment(comment_id):

    comment = CommentModel.find_by_id(comment_id)

    if comment:

        comment.delete_from_db()

        return {"Message":f"Comment with id {comment_id} was deleted"}
    
    return {"Message":f"There was no comment with an id of {comment_id} to delete"}

#this works
@comment_bp.route('/comments/<int:comment_id>',methods=['GET'])
def get_comment_by_id(comment_id):

    comment = CommentModel.find_by_id(comment_id)

    if comment:
        comment_to_return = comment.to_collections_dict()
        return comment_to_return
    
    return {"Message":f"There was no comment with an id of {comment_id}"}


#this works
@comment_bp.route('/comments',methods=['GET'])
def get_all_comments():

    comments =  CommentModel.find_all()

    if comments:
    
        comment_list = jsonify([{"comment":comment.to_collections_dict()} for comment in comments])
        
        return comment_list
    
    return {"Message":"There are no comments to return"}


#this works
@comment_bp.route('/posts/<int:post_id>/comments',methods=['GET'])
def get_all_comments_for_a_post(post_id):

    post = PostModel.find_by_id(post_id)

    if post:
        comments = db.session.query(CommentModel).filter(CommentModel.post_id == post_id).all()

        comment_list = jsonify([comment.to_collections_dict(post_id) for comment in comments])

        return comment_list
    
    return {"Message":f"There is no post with an id of {post_id}"}


@comment_bp.route('/replies/<int:comment_id>', methods=['POST'])
def write_reply(comment_id):

    comment = CommentModel.find_by_id(comment_id)

    if comment:
        data = request.get_json()

        reply = CommentModel(
            data['text'],
            data['post_id']

        )

        comment.replies.append(reply)

        try: 
            db.session.add(comment)
            db.session.commit()
        except:
            abort(500, message="Sorry buddy")

        return comment.to_collections_dict()
    
    return {"Message":f"There was no comment with an id of {comment_id} that you could reply to"}



    
    





    



