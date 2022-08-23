#импортируем все необходимое
from flask import Blueprint, render_template, request
from functions import get_post_by_word
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
from json import JSONDecodeError
import logging

#создаем главный блюпринт
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

@main_blueprint.route('/search')
def search_page():
    s = request.args['s']
    logging.info("Поиск данных")
    try:
        posts = get_post_by_word(s)
    except FileNotFoundError:
        logging.info("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Не удается загрузить файл"
    return render_template("post_list.html", posts=posts, word=s)
