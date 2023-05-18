from werkzeug.wrappers import Request, Response, ResponseStream
from config import config


class UserAuthMiddleware:
    '''
    Simple WSGI middleware
    '''

    res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        bearer = request.headers.get("Authorization")

        if bearer is None:
            return self.res(environ, start_response)

        secret = bearer.replace("Bearer ", "")

        if secret == config.BEARER:
            return self.app(environ, start_response)

        return self.res(environ, start_response)