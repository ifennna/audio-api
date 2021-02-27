from . import db

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
        assert value >= 0
        return value

    @db.validates('uploaded_time')
    def validate_uploaded_time(self, key, value):
        # check that time is not in the past
        return value

    def __repr__(self):
        return "<Audiobook '{}'>".format(self.title)