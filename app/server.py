from flask import Flask, Response

from app.src.create_image import create_cat_avatar


app = Flask(__name__)


@app.route('/<string:user_id>')
def create_cat_avatar(user_id):
    image = create_cat_avatar(user_id)
    return Response(image, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
