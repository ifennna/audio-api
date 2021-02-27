from flask_restplus import fields

class Dto:
    # request = {
    #     'audioFileType': fields.String(required=True, description='type of audio file'),
    #     'audioFileMetadata': fields.List()
    # }

    song = {
        'id': fields.Integer(required=True, description='song id'),
        'name': fields.String(required=True, description='song name'),
        'duration': fields.Integer(required=True, description='song duration in seconds'),
        'uploaded_time': fields.DateTime(description='time of song upload')
    }