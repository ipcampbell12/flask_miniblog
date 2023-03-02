from flask import Blueprint, request
from models import PostModel

post_bp = Blueprint("post", __name__)


@post_bp.route('/posts', methods=["POST"])
def create_post(data):

    post = PostModel(**data)

    post.save_to_db()

    return post


@post_bp.route('/posts/<ind:post_id>', methods=["PUT"])
def update_post(data, post_id):

    post = PostModel.find_by_id(post_id)

    if post:
        post.title = data["title"]
        post.text = data["text"]
    else:
        post = PostModel(id=post_id, **data)

    post.save_to_db()


@post_bp.route('/posts', methods=["GET"])
def get_all_posts():

    return PostModel.find_all()


@post_bp.route('/posts/<int:post_id>', methods=["GET"])
def get_post(post_id):

    return PostModel.find_by_id(post_id)


@post_bp.route('/posts/<int:post_id>', methods=["DELETE"])
def delete_post(post_id):
    PostModel.delete_from_db(post_id)
