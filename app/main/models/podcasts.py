from . import db

from ..errors.errors import ValidationError

class Podcasts(db.Model):
    __tablename__ = "podcasts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.PickleType, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False)

    @db.validates('duration')
    def validate_duration(self, key, value):
        if value < 0:
            raise ValidationError 

        return value

    @db.validates('host', 'name')
    def validate(self, key, value):
        if len(value) > 100:
            raise ValidationError

        return value

    @db.validates('participants')
    def validate_participants(self, key, value):
        if len(value) > 1:
            raise ValidationError
        
        for participant in value:
            if len(participant) > 100:
                raise ValidationError

        return value

    def __repr__(self):
        return "<Podcast '{}'>".format(self.name)