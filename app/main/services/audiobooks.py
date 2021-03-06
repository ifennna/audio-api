import datetime

from ..models import db
from ..models.audiobooks import Audiobooks

from ..errors.errors import ValidationError, ServerError


class AudiobookService:
    def add(self, data):
        required = ['title', 'duration', 'author', 'narrator']
        for item in required:
            if not item in data:
                raise ValidationError

        audiobook = Audiobooks(
            title=data['title'],
            duration=data['duration'],
            author=data['author'],
            narrator=data['narrator'],
            uploaded_time=datetime.datetime.utcnow()
        )

        try:
            self.__save(audiobook)
            return {
                'status': 'success',
                'message': 'Audiobook added successfully'
            }
        except Exception as e:
            raise ServerError

    def get(self, id):
        audiobook = Audiobooks.query.filter_by(id=id).first()

        if not audiobook:
            raise ValidationError

        return audiobook

    def getAll(self):
        return Audiobooks.query.all()

    def edit(self, id, data):
        fields = ['title', 'duration', 'author', 'narrator']
        audiobook = Audiobooks.query.filter_by(id=id).first()

        if not audiobook:
            raise ValidationError

        for field in fields:
            if field in data:
                setattr(audiobook, field, data[field])

        try:
            self.__save(audiobook)
            return {
                'status': 'success',
                'message': 'Audiobook edited successfully'
            }
        except Exception as e:
            raise ServerError

    def delete(self, id):
        audiobook = Audiobooks.query.filter_by(id=id).first()

        if not audiobook:
            raise ValidationError

        try:
            db.session.delete(audiobook)
            db.session.commit()

            return {
                'status': 'success',
                'message': 'Audiobook deleted successfully'
            }
        except Exception as e:
            raise ServerError

    def __save(self, data):
        db.session.add(data)
        db.session.commit()
