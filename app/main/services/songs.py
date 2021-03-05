import datetime

from ..models import db
from ..models.songs import Songs

from ..errors.errors import ValidationError, ServerError


class SongService:
    def add(self, song_data):
        if not 'name' in song_data or not 'duration' in song_data:
            raise ValidationError

        new_song = Songs(
            name=song_data['name'],
            duration=song_data['duration'],
            uploaded_time=datetime.datetime.utcnow()
        )

        try:
            self.__save(new_song)
            return {
                'status': 'success',
                'message': 'Song added successfully'
            }
        except Exception as e:
            raise ServerError

    def get(self, id):
        song = Songs.query.filter_by(id=id).first()

        if not song:
            raise ValidationError

        return song

    def getAll(self):
        return Songs.query.all()

    def edit(self, id, data):
        song = Songs.query.filter_by(id=id).first()

        if not song:
            raise ValidationError

        if 'name' in data:
            song.name = data['name']

        if 'duration' in data:
            song.duration = data['duration']

        try:
            self.__save(song)
            return {
                'status': 'success',
                'message': 'Song edited successfully'
            }
        except Exception as e:
            raise ServerError

    def delete(self, id):
        song = Songs.query.filter_by(id=id).first()

        if not song:
            raise ValidationError

        try:
            db.session.delete(song)
            db.session.commit()

            return {
                'status': 'success',
                'message': 'Song deleted successfully'
            }
        except Exception as e:
            raise ServerError

    def __save(self, data):
        db.session.add(data)
        db.session.commit()
