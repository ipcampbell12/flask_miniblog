from flask import Blueprint, request
from app.models import TagModel, PostModel

tag_bp = Blueprint("tag", __name__)


@tag_bp('/',methods=['POST'])
def create_tags(data):

    data =TagModel(**data)

    data.save_to_db()


@tag_bp('/<int:tag_id>/posts/<int:post_id>',methods=['POST'])
def add_tag_to_post(tag_id, post_id):

    post = PostModel.find_by_id(post_id)

    tag = TagModel.find_by_id(tag_id)

    post.tags.append(tag)

    return post
