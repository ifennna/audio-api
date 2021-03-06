from . import db

from ..errors.errors import ValidationError

class Audiobooks(db.Model):
    __tablename__ = "audiobooks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False)

    @db.validates('duration')
    def validate_duration(self, key, value):
        if value < 0:
            raise ValidationError 

        return value

    @db.validates('title', 'author', 'narrator')
    def validate(self, key, value):
        if len(value) > 100:
            raise ValidationError

        return value

    def __repr__(self):
        return "<Audiobook '{}'>".format(self.title)