from flask import request
from flask_restplus import Resource, Api

from ..services.songs import SongService
from ..dto.dto import Dto

SONG = 'song'
AUDIOBOOK = 'audiobook'
PODCAST = 'podcast'

api = Api()
dto = Dto(api)
song_service = SongService()

_song = dto.get_song_dto()
_req = dto.get_req_dto()


@api.route('/check')
class Check(Resource):
    def get(self):
        return {'message': 'hello'}


@api.route('/files/<audio_type>')
class Files(Resource):
    @api.marshal_list_with(_song, envelope='data')
    def get(self, audio_type):
        if audio_type == SONG:
            return song_service.getAll()
        else:
            api.abort(400)


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
