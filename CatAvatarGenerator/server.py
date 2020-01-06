import hashlib

from flask import Flask, render_template

from CatAvatarGenerator.src.create_image import create_cat_avatar

app = Flask(__name__)

salt = 'different salt for different website'


@app.route('/<string:user_id>')
def get_cat_avatar(user_id):
    salted_user_id = salt + user_id
    user_id_hash = hashlib.sha256(salted_user_id.encode()).hexdigest()

    cat_avatar_path = create_cat_avatar(user_id_hash)
    return render_template(
        'get_cat_avatar.html',
        avatar_image=cat_avatar_path
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
