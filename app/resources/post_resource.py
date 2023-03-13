from flask import Blueprint, request, jsonify
from app.models import PostModel, CommentModel
from app import db

post_bp = Blueprint("post", __name__)


@post_bp.route('/', methods=["POST"])
def create_post():

    data =request.get_json()
    print(data)
    post = PostModel(
        data["title"],
        data["text"],
    )

    post.save_to_db()

    #must return simple python dictionary
    return post.to_dict()


@post_bp.route('/<int:post_id>', methods=["PUT"])
def update_post(post_id):

    data = request.get_json()

    post = PostModel.find_by_id(post_id)

    if post:
        post.title = data["title"]
        post.text = data["text"]
    else:
        post = PostModel(id=post_id, **data)

    post.save_to_db()
    return post.to_dict()


@post_bp.route('/', methods=["GET"])
def get_all_posts():

    posts = PostModel.find_all()

    if posts:
        post_list = [post.to_collections_dict() for post in posts]
        return jsonify({"posts":post_list})
    
    return {"Message":"There are no posts to return"}

@post_bp.route('/<int:post_id>', methods=["GET"])
def get_post(post_id):

    post = PostModel.find_by_id(post_id)


    if post:
        post_to_return = post.to_collections_dict()
        return jsonify(post_to_return)
    
    return {"Message":f"There is no post with id of {post_id}"}



@post_bp.route('/<int:post_id>', methods=["DELETE"])
def delete_post(post_id):
    
    post = PostModel.find_by_id(post_id)


    if post:
    #the delete_from_db function works on the post object itself, not just the id
        post.delete_from_db()

        return {"message":f"The post with id {post_id} has been deleted"}
    
    
    return {"message":f"There was no post with an id of {post_id} to delete"}




@post_bp.route('/<string:post_name>', methods=["GET"])
def get_posts_by_name(post_name):

    posts = db.session.query(PostModel).filter(PostModel.title.ilike(f'%{post_name}%')).all()
    
    if posts:
        post_list = jsonify([{"posts":post.to_collections_dict()} for post in posts])
        return post_list
    
    return {"Message":f"There are no posts containing the keyword '{post_name}'"}
