from flask import Blueprint, render_template, request
from db.db_manager import DatabaseManager

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=['GET'])
def index():
    film = request.args.get('film', '').strip()
    actor = request.args.get('actor', '').strip()
    category = request.args.get('category', '').strip()
    year = request.args.get('year', '').strip()

    with DatabaseManager() as db:
        if film:
            db.save_search_query(film, "keyword")
        if actor:
            db.save_search_query(actor, "actor")
        if category:
            db.save_search_query(category, "genre")
        if year:
            db.save_search_query(year, "year")
        results = db.get_movies(film, actor, category, year)
        popular_queries = db.get_popular_queries()

    return render_template('index.html', results=results, popular_queries=popular_queries)