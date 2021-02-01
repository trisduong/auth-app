from flask import request, Blueprint
from .tool import login_required, check, crawl_url, logout

app = Blueprint('app', __name__)


@app.route('/top')
@login_required
def crawl_trending():
    url = 'https://stackshare.io/tools/trending'
    return crawl_url(url)


@app.route('/logout')
def logout():
    if check(request.headers.get('Authorization')):
        return logout()
    else:
        return 'You logout successful'


@app.route('/health')
def health():
    return 'ok'
