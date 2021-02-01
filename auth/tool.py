from flask import current_app, request, Response
import base64
from functools import wraps


def check(author_header):
    if 'AUTH_USERNAME' in current_app.config:
        username = current_app.config['AUTH_USERNAME']
    else:
        username = 'admin'
    if 'AUTH_PASSWORD' in current_app.config:
        password = current_app.config['AUTH_PASSWORD']
    else:
        password = 'admin'
    encoded_uname_pass = author_header.split()[-1]
    if encoded_uname_pass == base64.b64encode(str.encode(':'.join([username, password]))).decode():
        return True


def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        author_header = request.headers.get('Authorization')
        if author_header and check(author_header):
            return f(*args, **kwargs)
        else:
            resp = Response()
            resp.headers['WWW-Authenticate'] = 'Basic realm="Login required"'
            return resp, 401
    return decorator
