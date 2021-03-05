from flask import request
from flask_restplus import Resource, Api

from ..services.songs import SongService
from ..errors.errors import ValidationError, ServerError
from ..dto.dto import Dto

SONG = 'song'
AUDIOBOOK = 'audiobook'
PODCAST = 'podcast'

api = Api()
dto = Dto(api)
song_service = SongService()

_song = dto.get_song_dto()
_req = dto.get_req_dto()


@api.errorhandler(ValidationError)
@api.errorhandler(ServerError)
def handle_error(error):
    return error.to_dict(), getattr(error, 'code')

@api.errorhandler
def default_error_handler(error):
    print(error)
    error = ServerError()
    return error.to_dict(), getattr(error, 'code', 500)


@api.route('/files/<audio_type>')
class Files(Resource):
    @api.marshal_list_with(_song, envelope='data')
    def get(self, audio_type):
        if audio_type == SONG:
            return song_service.getAll()
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
        else:
            api.abort(400)


@api.route('/files/<audio_type>/<audio_id>')
class FileManage(Resource):
    @api.expect(_req, validate=True)
    def put(self, audio_type, audio_id):
        data = request.json
        if audio_type == SONG:
            return song_service.edit(audio_id, data['audioFileMetadata'])
        else:
            api.abort(400)

    def delete(self, audio_type, audio_id):
        if audio_type == SONG:
            return song_service.delete(audio_id)
        else:
            api.abort(400)

    @api.marshal_list_with(_song, envelope='data')
    def get(self, audio_type, audio_id):
        if audio_type == SONG:
            return song_service.get(audio_id)
        else:
            api.abort(400)
