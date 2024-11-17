from flask import Flask
from flask_session import Session

from config import Config
from app.extensions import db
from app.utils import DBUtils, ROUTES

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SESSION_SQLALCHEMY'] = db
    
    db.init_app(app)
    
    @app.context_processor
    def inject_routes():
        """Inject ROUTES dictionary into all templates."""
        return {'ROUTES': ROUTES}
    
    #models_setup()
    DBUtils.drop_db(app)
    DBUtils.setup_db(app)

    # Initialize Flask extensions here
    Session(app)
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix="/users")

    return app