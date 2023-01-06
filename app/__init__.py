from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import configs


db = SQLAlchemy()
migrate = Migrate()


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])
    app.url_map.strict_slashes = False


    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import Article, Entry, Category

    with app.app_context():
        from app import views

    from app.routes import entry_bp, root_bp, category_bp, article_bp
    app.register_blueprint(root_bp)
    app.register_blueprint(entry_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(article_bp)

    return app
