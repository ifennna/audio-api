import datetime

from ..models import db
from ..models.songs import Songs


class SongService:
    def add(self, song_data):
        new_song = Songs(
            name=song_data['name'],
            duration=song_data['duration'],
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

    def edit(self, id, data):
        song = Songs.query.filter_by(id=id).first()
        
        if 'name' in data:
            song.name = data['name']
            
        if 'duration' in data:
            song.duration = data['duration']

        self.__save(song)
        response = {
            'status': 'success',
            'message': 'Song edited successfully'
        }

        return response

    def delete(self, id):
        print("moo")

    def __save(self, data):
        db.session.add(data)
        db.session.commit()
