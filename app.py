import flask
import common.ptt_data as ptt
from flask import jsonify
from flask_caching import Cache
from resources.ptt_user import PttUser

app = flask.Flask(__name__)
app.config.update(
    DEBUG=True,
    JSON_AS_ASCII=False
)
cache = Cache(app, config={'CACHE_TYPE': 'simple',
                           "CACHE_DEFAULT_TIMEOUT": 300})


@app.route('/', methods=['GET'])
def home():
    return "<h1>PttData Works!</h1>"


@cache.cached(timeout=120)
@app.route('/user/<string:id>', methods=['GET'])
def getUser(id=None):
    if id is not None:
        user = cache.get(id)
        if user is None:
            user = PttUser(id).get()
            cache.set(id, user)
    return jsonify(user)


@cache.cached(timeout=120)
@app.route('/post/<string:id>', methods=['GET'])
def getUserPosts(id=None):
    if id is not None:
        posts = cache.get(id+"post")
        if posts is None:
            posts = []
            PttUser(id).get_posts(
                lambda post: posts.append(ptt.createPost(post)))
            cache.set(id+"post", posts)
    return jsonify(posts)


if __name__ == '__main__':
    app.run()
