from flask import request
from functools import wraps
from flask_restplus import Resource, Api, marshal_with

from ..dto.dto import Dto
from ..services.songs import SongService
from ..services.podcasts import PodcastService
from ..services.audiobooks import AudiobookService
from ..errors.errors import ValidationError, ServerError

SONG = 'song'
PODCAST = 'podcast'
AUDIOBOOK = 'audiobook'

api = Api()
dto = Dto(api)
song_service = SongService()
podcast_service = PodcastService()
audiobook_service = AudiobookService()

_req = dto.get_req_dto()
_song = dto.get_song_dto()
_podcast = dto.get_podcast_dto()
_audiobook = dto.get_audiobook_dto()


@api.errorhandler(ServerError)
@api.errorhandler(ValidationError)
def handle_error(error):
    return error.to_dict(), getattr(error, 'code')


@api.errorhandler
def default_error_handler(error):
    error = ServerError()
    return error.to_dict(), getattr(error, 'code', 500)


def dynamic_marshal_with(songDto, podcastDto, audiobookDto):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            audio_type = kwargs['audio_type']
            if audio_type == SONG:
                model = songDto
            elif audio_type == PODCAST:
                model = podcastDto
            elif audio_type == AUDIOBOOK:
                model = audiobookDto

            func_two = marshal_with(model, envelope='data')(func)

            return func_two(*args, **kwargs)
        return wrapper
    return decorator


@api.route('/files/<audio_type>')
class Files(Resource):
    @dynamic_marshal_with(_song, _podcast, _audiobook)
    def get(self, audio_type):
        if audio_type == SONG:
            return song_service.getAll()
        elif audio_type == PODCAST:
            return podcast_service.getAll()
        elif audio_type == AUDIOBOOK:
            return audiobook_service.getAll()
        else:
            raise ValidationError


@api.route('/files')
class FileCreate(Resource):
    @api.expect(_req, validate=True)
    def post(self):
        data = request.json
        audio_type = data['audioFileType']
        if audio_type == SONG:
            return song_service.add(data['audioFileMetadata'])
        elif audio_type == PODCAST:
            return podcast_service.add(data['audioFileMetadata'])
        elif audio_type == AUDIOBOOK:
            return audiobook_service.add(data['audioFileMetadata'])
        else:
            raise ValidationError


@api.route('/files/<audio_type>/<audio_id>')
class FileManage(Resource):
    @api.expect(_req, validate=True)
    def put(self, audio_type, audio_id):
        data = request.json
        if audio_type == SONG:
            return song_service.edit(audio_id, data['audioFileMetadata'])
        elif audio_type == PODCAST:
            return podcast_service.edit(audio_id, data['audioFileMetadata'])
        elif audio_type == AUDIOBOOK:
            return audiobook_service.edit(audio_id, data['audioFileMetadata'])
        else:
            raise ValidationError

    def delete(self, audio_type, audio_id):
        if audio_type == SONG:
            return song_service.delete(audio_id)
        elif audio_type == PODCAST:
            return podcast_service.delete(audio_id)
        elif audio_type == AUDIOBOOK:
            return audiobook_service.delete(audio_id)
        else:
            raise ValidationError

    @dynamic_marshal_with(_song, _podcast, _audiobook)
    def get(self, audio_type, audio_id):
        if audio_type == SONG:
            return song_service.get(audio_id)
        elif audio_type == PODCAST:
            return podcast_service.get(audio_id)
        elif audio_type == AUDIOBOOK:
            return audiobook_service.get(audio_id)
        else:
            raise ValidationError
