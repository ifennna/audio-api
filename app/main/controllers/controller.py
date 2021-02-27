from flask import request
from flask_restplus import Resource, Api

from ..services.songs import SongService

api = Api()


@api.route('/check')
class Check(Resource):
    def get(self):
        return {'message': 'hello'}


@api.route('/files')
class Files(Resource):
    def get(self):
        SongService.getAll()
