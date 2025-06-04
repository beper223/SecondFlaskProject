from .main import main_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)# url_prefix='/admin'
    # app.register_blueprint(admin_bp, url_prefix='/admin')
    # app.register_blueprint(api_bp, url_prefix='/api/v1')