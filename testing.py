import unittest
# import flask_unittest
from app import create_app, db
from app.models import PostModel, CommentModel, TagModel
from app.resources.tag_resource import search_for_posts_by_tagname
import json
from flask import jsonify

class TestConfig():
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestAllTheThings(unittest.TestCase):
    # app = create_app()

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    
    def createPosts(self):
        p1 = PostModel(title="Cool Title",text="Here some fun text")
        p2 = PostModel(title="Lame Title",text="Here some lame text")

        posts = [p1, p2]

        for post in posts:
            db.session.add(post)
        
        db.session.commit()

        return posts

    def createComments(self):
        c1 = CommentModel(text="Your post is really cool", post_id=1)
        c2 = CommentModel(text="Your post is really lame", post_id=2)

        comments = [c1,c2]

        for comment in comments: 
            db.session.add(comment)

        db.session.commit()

        return comments

    def createTags(self):
        t1 = TagModel(name = "Cool")
        t2 = TagModel(name = "Lame")

        tags = [t1,t2]

        for tag in tags: 
            db.session.add(tag)
        
        db.session.commit()

        return tags

    
    def testPosts(self):
        
        posts = self.createPosts()
    
        self.assertEqual(posts[0].title, "Cool Title")
        self.assertEqual(posts[1].title, "Lame Title")
        self.assertEqual(posts[0].text, "Here some fun text")
        self.assertEqual(posts[1].text, "Here some lame text")
    
    def testComments(self):
        posts = self.createPosts()
        comments = self.createComments()

        pc1 = posts[0].comments.all()
        pc2 = posts[1].comments.all()

        self.assertEqual(pc1, [comments[0]])
        self.assertEqual(pc2, [comments[1]])
    
    def testTags(self):
        
        tags = self.createTags()

        self.assertEqual(tags[0].name, "Cool")
        self.assertEqual(tags[1].name, "Lame")
    
    #need to start function mae with "test"
    def testTaggingPosts(self):
        posts = self.createPosts()
        tags = self.createTags()

        posts[0].tags.append(tags[0])
        posts[0].tags.append(tags[1])
        posts[1].tags.append(tags[1])

        #works if you remove .all(),  maybe because it uses many to man association table??
        pt1 = posts[0].tags
        pt2 = posts[1].tags

        self.assertEqual(pt1, [tags[0],tags[1]])
        self.assertEqual(pt2, [tags[1]])
    
    def testGetPostByTag(self):
        posts = self.createPosts()
        tags = self.createTags()

        posts[0].tags.append(tags[0])
        posts[0].tags.append(tags[1])
        posts[1].tags.append(tags[1])

        tester = self.app.test_client(self)

        tag_name = tags[0].name

        response = tester.get(f'/tags/{tag_name}/posts', content_type="application/json")

        self.assertEqual(response.get_json(), [{'post':posts[0].to_dict()}])

    def testGetPostByName(self):
        posts = self.createPosts()

        tester = self.app.test_client(self)

        search = "title"

        response = tester.get(f'/posts/{search}', content_type="application/json")

        #should return the same thing your route would return

        self.assertEqual(response.get_json(), [{"posts":post.to_collections_dict()} for post in posts])


    
        



if __name__ == '__main__':
    unittest.main(verbosity=2)