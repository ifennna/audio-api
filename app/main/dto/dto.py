from flask_restplus import fields


class Dto:
    audio_file = {
        'name': fields.String,
        'title': fields.String,
        'author': fields.String,
        'narrator': fields.String,
        'host': fields.String,
        'participants': fields.List(fields.String),
        'duration': fields.Integer(required=True)
    }

    song = {
        'id': fields.Integer(required=True, description='song id'),
        'name': fields.String(required=True, description='song name'),
        'duration': fields.Integer(required=True, description='song duration in seconds'),
        'uploaded_time': fields.DateTime(description='time of song upload')
    }

    def __init__(self, api):
        self.api = api

    def get_req_dto(self):
        nested_dto = self.api.model('File', self.audio_file)

        return self.api.model('Request', {
            'audioFileType': fields.String(required=True),
            'audioFileMetadata': fields.Nested(nested_dto, required=True)
        })

    def get_song_dto(self):
        return self.api.model('Song', self.song)
