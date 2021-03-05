class BaseError(Exception):
    def __init__(self, code=400, message='', status=''):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status

    def to_dict(self):
        return {'message': self.message,
                'status': self.status, }


class ValidationError(BaseError):
    def __init__(self, message='Bad Request'):
        BaseError.__init__(self)
        self.code = 400
        self.message = message
        self.status = 'error'

class ServerError(BaseError):
    def __init__(self, message='Internal Server Error'):
        BaseError.__init__(self)
        self.code = 500
        self.message = message
        self.status = 'error'
