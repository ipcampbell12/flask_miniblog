from flask import Blueprint, request

from models import CommentModel, PostModel

comment_bp = Blueprint("comment", __name__)


@comment_bp.route('/posts/post_id/comments', methods=['POST'])
def write_comment(data, post_id):
    post = PostModel.find_by_id(post_id)

    comment = CommentModel(**data)

    post.append(comment)

    return comment
