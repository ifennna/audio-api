import datetime

from ..models import db
from ..models.songs import Songs


class SongService:
    def add(self, song_data):
        new_song = Song(
            name=data['name'],
            duration=data['name'],
            uploaded_time=datetime.datetime.utcnow()
        )

        self.__save(new_song)
        response = {
            'status': 'success',
            'message': 'Song added successfully'
        }

        return response

    def get(self, id):
        return Songs.query.filter_by(id=id).first()

    def getAll(self):
        return Songs.query.all()

    def edit(self, data):
        print("mo")

    def delete(self, id):
        print("moo")

    def __save(data):
        db.session.add(data)
        db.session.commit()
