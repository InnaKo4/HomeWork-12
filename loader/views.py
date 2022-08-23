#импортируем все необходимое
from flask import Blueprint, render_template, request
from functions import add_post
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
import logging

#создаем блюпринт загрузки файла
@loader_blueprint.route('/post')
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=["POST"])
def add_post_page():
    content = request.form["content"]
    picture = request.files.get("picture")
    filename = picture.filename
    picture_path = f"./uploads/images/{filename}"
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    extension = filename.split(".")[-1]
    if extension not in allowed_extensions:
        return f"Файлы типа {extension} не поддерживаются"
    elif not picture or not content:
        logging.info('Загруженный файл не является изображением')
        return "Ошибка при загрузке файла"
    else:
        pass
    try:
        picture.save(picture_path)
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "Файл не найден"
    post = {"pic": picture_path, "content": content}
    add_post(post)
    return render_template("post_uploaded.html", post=post)