from flask import Blueprint, request, jsonify
from app.models import TagModel, PostModel, posts_tags
from flask_smorest import abort
from app import db

tag_bp = Blueprint("tag", __name__)

#this one works
@tag_bp.route('/tags',methods=['POST'])
def create_tags():

    
    data = request.get_json()
    
    tag = TagModel(
        data['name']
    )

    tag.save_to_db()

    return tag.to_dict()

#this one works
@tag_bp.route('/posts/<int:post_id>/tags/<int:tag_id>',methods=['POST'])
def add_tag_to_post(tag_id, post_id):

    post = PostModel.find_by_id(post_id)

    tag = TagModel.find_by_id(tag_id)

    post.tags.append(tag)
    
    try: 
        db.session.add(post)
        db.session.commit()
    except:
        abort(500, message="Sorry buddy")
    

    return post.to_dict()

#this one works
@tag_bp.route('/posts/<int:post_id>/tags/<int:tag_id>',methods=['DELETE'])
def remove_tag_from_post(tag_id, post_id):

    post = PostModel.find_by_id(post_id)

    tag = TagModel.find_by_id(tag_id)

    post.tags.remove(tag)
    
    try: 
        db.session.add(post)
        db.session.commit()
    except:
        abort(500, message="Sorry buddy")
    
    return {"message":f"The tag with id {tag_id} was removed from the post with id {post_id}"}

#this one works
@tag_bp.route('/tags/<string:tag_name>/posts',methods=['GET'])
def search_for_posts_by_tagname(tag_name):
    
    posts = db.session.query(PostModel, posts_tags).filter(TagModel.name == tag_name).filter(TagModel.id == posts_tags.c.tag_id).filter(posts_tags.c.post_id == PostModel.id).all()

    post_list = jsonify([{"post":post[0].to_dict()} for post in posts])

    return post_list

#this one works
@tag_bp.route('/tags/<int:tag_id>/posts',methods=['GET'])
def search_for_posts_by_tagid(tag_id):
    
    posts = db.session.query(PostModel, posts_tags).filter(PostModel.id == posts_tags.c.post_id).filter(posts_tags.c.tag_id == tag_id)

    post_list = jsonify([{"post":post[0].to_dict()} for post in posts])

    return post_list

#this one works
@tag_bp.route('/tags',methods=['GET'])
def get_all_tags():

    tags = TagModel.find_all()

    tag_list = jsonify([{"tag":tag.to_dict()} for tag in tags])

    return tag_list

#this one works
@tag_bp.route('/posts/<int:post_id>/tags',methods=['GET'])
def get_tags_by_post(post_id):

    tags = db.session.query(TagModel, posts_tags).filter(TagModel.id == posts_tags.c.tag_id).filter(posts_tags.c.post_id == post_id)
    
    tag_list = jsonify([{"tag":tag[0].to_dict()} for tag in tags])
   
    return tag_list