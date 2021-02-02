from flask import request, Blueprint, redirect
from .tool import login_required, check, crawl_url
import secrets

app_auth = Blueprint('app_auth', __name__)


class Register_route(object):
    def __init__(self, app=None, blueprint=None):
        self.blueprint = blueprint
        if app is not None and blueprint is not None:
            self.init_app(app, blueprint)

    @staticmethod
    def init_app(app, blueprint):
        app.register_blueprint(blueprint)


@app_auth.route('/top')
@login_required
def crawl_trending():
    url = 'https://stackshare.io/tools/trending'
    return crawl_url(url)


@app_auth.route('/logout')
def logout():
    if check(request.headers.get('Authorization')):
        host = request.headers.get('Host')
        url = 'http://' + secrets.token_urlsafe(16) + ':' + secrets.token_urlsafe(16) + '@' + host + '/logout'
        return redirect(url), 401
    else:
        return 'Success'


@app_auth.route('/health')
def health():
    return 'ok'
