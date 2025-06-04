from .main import main_bp
from .about import about_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)# url_prefix='/admin'
    app.register_blueprint(about_bp,url_prefix='/about')
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    # app.register_blueprint(api_bp, url_prefix='/api/v1')