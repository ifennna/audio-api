from . import db

class Songs(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    uploaded_time = db.Column(db.DateTime, nullable=False)

    @db.validates('duration')
    def validate_duration(self, key, value):
        assert value >= 0
        return value

    def __repr__(self):
        return "<Song '{}'>".format(self.name)