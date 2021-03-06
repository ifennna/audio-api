import datetime

from ..models import db
from ..models.podcasts import Podcasts

from ..errors.errors import ValidationError, ServerError


class PodcastService:
    def add(self, data):
        required = ['name', 'duration', 'host']
        for item in required:
            if not item in data:
                raise ValidationError

        if not 'participants' in data:
            participants = ''
        else:
            participants = ', '.join(data['participants'])

        podcast = Podcasts(
            name=data['name'],
            duration=data['duration'],
            host=data['host'],
            participants=participants,
            uploaded_time=datetime.datetime.utcnow()
        )

        try:
            self.__save(podcast)
            return {
                'status': 'success',
                'message': 'Podcast added successfully'
            }
        except Exception as e:
            raise ServerError(e)

    def get(self, id):
        podcast = Podcasts.query.filter_by(id=id).first()

        if not podcast:
            raise ValidationError

        return self.__extract(podcast)

    def getAll(self):
        podcasts = Podcasts.query.all()

        response = []

        for podcast in podcasts:
            response.append(self.__extract(podcast)) 

        return response

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

    def __extract(self, podcast):
        response = {
            'id': podcast.id,
            'name': podcast.name,
            'host': podcast.host,
            'duration': podcast.duration,
            'uploaded_time': podcast.uploaded_time
        }

        if podcast.participants == '':
            response['participants'] = []
        else:
            response['participants'] = podcast.participants.split(', ')   

        return response   
