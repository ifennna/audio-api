from flask import request
from flask_restplus import Resource, Api

from ..services.songs import SongService
from ..dto.dto import Dto

SONG = 'song'

api = Api()
_song = Dto.song
# _req = Dto.request


@api.route('/check')
class Check(Resource):
    def get(self):
        return {'message': 'hello'}


@api.route('/files/<audio_type>')
class Files(Resource):
    @api.marshal_list_with(_song, envelope='data')
    def get(self, audio_type):
        if audio_type == SONG:
            return SongService.getAll()
        else:
            api.abort(400)

    def post(self):
        data = request.json
        return SongService.add(data)
