from flask import Flask, render_template

from app.src.create_image import create_cat_avatar

app = Flask(__name__)


@app.route('/<string:user_id>')
def get_cat_avatar(user_id):
    cat_avatar_path = create_cat_avatar(user_id)
    return render_template(
        'get_cat_avatar.html',
        avatar_image=cat_avatar_path
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
