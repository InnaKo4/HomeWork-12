#импортируем все нужное нам: функции, блюпринты, логгинг
from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint
import logging
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
#регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

#добавляем логгинг
logging.basicConfig(filename="info.log", level=logging.INFO)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

