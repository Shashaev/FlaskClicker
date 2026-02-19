import pathlib

import flask
import requests

import image


base_bp = flask.Blueprint('base', __name__)


@base_bp.route('/')
def index():
    return flask.render_template('index.html')


@base_bp.route('/edge_<number>')
def end(number):
    return flask.render_template('end.html', number=number)


@base_bp.route('/number_<number>')
def get_image_page(number):
    local_path = pathlib.Path(f'src/static/images/img_{number}.jpg')
    number = int(number)
    try:
        if not local_path.exists():
            url = (
                'https://yandex.ru/images/search?'
                f'text=цифра_{number}&from=tabbar'
            )
            path = requests.get(url).text
            path = 'https://' + path.split("src='//")[1].split("'")[0]
            image.save_image(requests.get(path).content, local_path)

        local_path = pathlib.Path(f'static/images/img_{number}.jpg')
        return flask.render_template(
            'basic_page.html',
            src=local_path,
            old_number=number,
            number=number + 1,
        )
    except IndexError:
        return flask.redirect(flask.url_for('end', number=number))
