from flask import Blueprint, request

from ..models.comment import CommentModel
from ..models.post import PostModel

comment_bp = Blueprint("comment", __name__)


@comment_bp.route('/posts/<int:id>/comments', methods=['POST'])
def write_comment(data, post_id):
    post = PostModel.find_by_id(post_id)

    comment = CommentModel(**data)

    post.append(comment)

    return comment
