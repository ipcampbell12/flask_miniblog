import unittest
from app import create_app, db
from app.models import PostModel, CommentModel, TagModel


class TestConfig():
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TestAllTheThings(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # @staticmethod
    # def createPosts():

    # @staticmethod
    # def createComments():

    # @staticmethod
    # def createTags():

    
    def testPosts(self):
        p1 = PostModel(title="Cool Title",text="Here some fun text")
        p2 = PostModel(title="Lame Title",text="Here some lame text")
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        self.assertEqual(p1.title, "Cool Title")
        self.assertEqual(p2.title, "Lame Title")
        self.assertEqual(p1.text, "Here some fun text")
        self.assertEqual(p2.text, "Here some lame text")
    
    def testComments(self):
        p1 = PostModel(title="Cool Title",text="Here some fun text")
        p2 = PostModel(title="Lame Title",text="Here some lame text")
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        c1 = CommentModel(text="Your post is really cool", post_id=1)
        c2 = CommentModel(text="Your post is really lame", post_id=2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        pc1 = p1.comments.all()
        pc2 = p2.comments.all()

        self.assertEqual(pc1, [c1])
        self.assertEqual(pc2, [c2])
    
    def testTags(self):
        t1 = TagModel(name = "Cool")
        t2 = TagModel(name = "Lame")
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        self.assertEqual(t1.name, "Cool")
        self.assertEqual(t2.name, "Lame")
    
    #need to start function mae with "test"
    def testTaggingPosts(self):
        p1 = PostModel(title="Cool Title",text="Here some fun text")
        p2 = PostModel(title="Lame Title",text="Here some lame text")
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        t1 = TagModel(name = "Cool")
        t2 = TagModel(name = "Lame")
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        #need to append tags to posts first
        p1.tags.append(t1)
        p2.tags.append(t2)
        p1.tags.append(t2)
        p2.tags.append(t1)

        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        #works if you remove .all(),  maybe because it uses many to man association table??
        pt1 = p1.tags
        pt2 = p2.tags

        self.assertEqual(pt1, [t1,t2])
        self.assertEqual(pt2, [t2,t1])
    
    
        



if __name__ == '__main__':
    unittest.main(verbosity=2)