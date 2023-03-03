from flask import Blueprint, request, jsonify
from app.models import PostModel
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


@post_bp.route('/', methods=["GET"])
def get_all_posts():

    posts = db.session.query(PostModel).all()
    
    # post_list = [jsonify(post) for post in posts]
    return 

@post_bp.route('/<int:post_id>', methods=["GET"])
def get_post(post_id):

    post = PostModel.find_by_id(post_id).to_dict()
    response = jsonify(post)

    return response


@post_bp.route('/<int:post_id>', methods=["DELETE"])
def delete_post(post_id):
    PostModel.delete_from_db(post_id)


@post_bp.route('/search/posts/post_name', methods=["GET"])
def get_posts_by_name(post_name):
    
    return PostModel.find_by_title(post_name)

