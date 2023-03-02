from flask import Blueprint, request
from app.models import TagModel, PostModel
from flask_smorest import abort
from app import db

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
    
    try: 
        db.session.add(post)
        db.session.commit()
    except:
        abort(500, message="Sorry buddy")

@tag_bp('/<int:tag_id>/posts/<int:post_id>',methods=['DELETE'])
def add_tag_to_post(tag_id, post_id):

    post = PostModel.find_by_id(post_id)

    tag = TagModel.find_by_id(tag_id)

    post.tags.remove(tag)
    
    try: 
        db.session.add(post)
        db.session.commit()
    except:
        abort(500, message="Sorry buddy")


@tag_bp('/search/tags/tag_name/posts',methods=['GET'])
def serach_for_posts_by_tagname(tag_name):
    
    posts = db.sesion.query(PostModel).filter_by(PostModel.tags.name == tag_name).all()

    return posts