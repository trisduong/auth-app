from flask import request, redirect, Blueprint
import secrets
import requests
from bs4 import BeautifulSoup
from auth.tool import login_required, check

app = Blueprint('app', __name__)


@app.route('/top')
@login_required
def crawl_trending():
    resp = requests.get('https://stackshare.io/tools/trending')
    tree = BeautifulSoup(markup=resp.text, features="html5lib")
    nodes = tree.find_all(name='span', attrs={'id': 'service-name-trending'})
    count = 1
    stack_text = '<ul>'
    for node in nodes:
        Stack = str(node)[(str(node).find('">') + 2): str(node).find('</')]
        stack_text += '<li>' + str(count) + '- ' + Stack + '</li>'
        count += 1
    stack_text += '</ul>'
    return stack_text


@app.route('/logout')
def logout():
    if check(request.headers.get('Authorization')):
        host = request.headers.get('Host')
        url = 'http://' + secrets.token_urlsafe(16) + ':' + secrets.token_urlsafe(16) + '@' + host + '/logout'
        return redirect(url)
    else:
        return 'You logout successful'


@app.route('/health')
def health():
    return 'ok'
