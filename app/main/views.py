from . import main
from Flask import render_template, url_for, request

@main.route("/")
def index():
    arg = {
    'title': "主页"
    }
    return render_template('main/index.html',arg=arg),
