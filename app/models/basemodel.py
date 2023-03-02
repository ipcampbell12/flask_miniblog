from app import db
from flask_smorest import abort


class BaseModel(db.Model):
    __abstract__ = True

    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            abort(500, f"There was an error saving {self} to the database")

    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            abort(500, f"There was an error saving {self} to the database")

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
