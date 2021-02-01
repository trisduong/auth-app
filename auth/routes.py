from flask import request, Blueprint
from .tool import login_required, check, crawl_url, logout

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
        return logout()
    else:
        return 'You logout successful'


@app_auth.route('/health')
def health():
    return 'ok'
