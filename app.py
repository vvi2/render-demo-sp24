from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/', prefix='static/', index_file='index.htm', autorefresh=True)


@app.route('/', methods=['GET'])
def hello():
    return make_response("Hello, world!!!!!!!!!!!")


@app.route('/secretonethatdoesntexist', methods=['GET'])
def secret():
    return make_response("Shhhh, this is a secret.")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)
