import datetime

from ..models import db
from ..models.podcasts import Podcasts

from ..errors.errors import ValidationError, ServerError


class PodcastService:
    def add(self, data):
        required = ['name', 'duration', 'host', 'participants']
        for item in required:
            if not item in data:
                raise ValidationError

        podcast = Podcasts(
            name=data['name'],
            duration=data['duration'],
            host=data['host'],
            participants=data['participants'],
            uploaded_time=datetime.datetime.utcnow()
        )

        try:
            self.__save(podcast)
            return {
                'status': 'success',
                'message': 'Podcast added successfully'
            }
        except Exception as e:
            raise ServerError

    def get(self, id):
        podcast = Podcasts.query.filter_by(id=id).first()

        if not podcast:
            raise ValidationError

        return podcast

    def getAll(self):
        return Podcasts.query.all()

    def edit(self, id, data):
        fields = ['name', 'duration', 'host', 'participant']
        podcast = Podcasts.query.filter_by(id=id).first()

        if not podcast:
            raise ValidationError

        for field in fields:
            if field in data:
                setattr(podcast, field, data[field])

        try:
            self.__save(podcast)
            return {
                'status': 'success',
                'message': 'Podcast edited successfully'
            }
        except Exception as e:
            raise ServerError

    def delete(self, id):
        podcast = Podcasts.query.filter_by(id=id).first()

        if not podcast:
            raise ValidationError

        try:
            db.session.delete(podcast)
            db.session.commit()

            return {
                'status': 'success',
                'message': 'Podcast deleted successfully'
            }
        except Exception as e:
            raise ServerError

    def __save(self, data):
        db.session.add(data)
        db.session.commit()
