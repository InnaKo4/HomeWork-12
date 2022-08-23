import json


def load_posts():
    """Загружает данные из Json в Python"""
    with open("posts.json", "r") as file:
        file_json = file.read()
        all_posts = json.loads(file_json)
        return all_posts


def get_post_by_word(word):
    """Выполняет поиск постов по слову"""
    posts = load_posts()
    all_posts = []
    for post in posts:
        if word.lower() in post['content'].lower():
            all_posts.append(post)
    return all_posts

def add_post(post):
    """Добавляет новый пост в файл Json"""
    posts = load_posts()
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file)