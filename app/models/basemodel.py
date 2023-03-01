from app import db
from flask_smorest import abort


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            abort(500, message=f"There was an error adding {self} ")

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            abort(500, f"{self}could not be deleted")

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
