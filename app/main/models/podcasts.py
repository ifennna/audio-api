from . import db

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
        assert value >= 0
        return value

    @db.validates('participants')
    def participants(self, key, value):
        assert len(value) <= 10
            # raise ValueError("maximum nuber of supported participans is 10")
        
        for participant in value:
            assert len(participant) <= 100

        self.participants = participants

    def __repr__(self):
        return "<Podcast '{}'>".format(self.name)