import hashlib

from flask import Flask, render_template
import redis

from CatAvatarGenerator.src.create_image import create_cat_avatar
from CatAvatarGenerator.settings.config import SALT

app = Flask(__name__)

cache = redis.StrictRedis(host='redis', port=6379)


@app.route('/<string:user_id>')
def get_cat_avatar(user_id):
    salted_user_id = SALT + user_id
    user_id_hash = hashlib.sha256(salted_user_id.encode()).hexdigest()

    avatar_image = cache.get(user_id)

    if avatar_image is None:
        avatar_image = create_cat_avatar(user_id_hash)
        cache.set(user_id, avatar_image)
    return render_template(
        'get_cat_avatar.html',
        avatar_image=avatar_image.decode("utf-8")
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
