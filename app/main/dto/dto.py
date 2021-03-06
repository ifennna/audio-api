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
        'id': fields.Integer(required=True),
        'name': fields.String(required=True),
        'duration': fields.Integer(required=True),
        'uploaded_time': fields.DateTime
    }

    podcast = {
        'id': fields.Integer(required=True),
        'name': fields.String(required=True),
        'host': fields.String(required=True),
        'participants': fields.List(fields.String, required=True),
        'duration': fields.Integer(required=True),
        'uploaded_time': fields.DateTime
    }

    audiobook = {
        'id': fields.Integer(required=True),
        'title': fields.String(required=True),
        'author': fields.String(required=True),
        'narrator': fields.String(required=True),
        'duration': fields.Integer(required=True),
        'uploaded_time': fields.DateTime
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

    def get_podcast_dto(self):
        return self.api.model('Podcast', self.podcast)

    def get_audiobook_dto(self):
        return self.api.model('Audiobook', self.audiobook)
