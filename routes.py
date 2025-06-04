from flask import Blueprint, render_template, request
from db.db_manager import DatabaseManager
# from . import auth_bp  # Импорт Blueprint из текущего модуля

# Создаём Blueprint с именем 'search' и префиксом URL '/search'
# from flask import Blueprint
main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    film = request.args.get('film', '').strip()
    actor = request.args.get('actor', '').strip()
    category = request.args.get('category', '').strip()
    year = request.args.get('year', '').strip()

    with DatabaseManager() as db:
        if film:
            db.save_search_query(film,"keyword")
        if actor:
            db.save_search_query(actor,"actor")
        if category:
            db.save_search_query(category,"genre")
        if year:
            db.save_search_query(year,"year")
        results = db.get_movies(film,actor,category,year)
        popular_queries = db.get_popular_queries()

    return render_template('index.html', results=results, popular_queries=popular_queries)


@main.route('/about')
def about():  # put application's code here
    return render_template('about.html')