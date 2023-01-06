from flask import Blueprint

from app.views.entries import EntryView
from app.views.articles import CategoryView, ArticleView


root_bp = Blueprint("root", __name__)

entry_view = EntryView.as_view("entry_view")
entry_bp = Blueprint("entries", __name__, url_prefix="/entries")
entry_bp.add_url_rule("/", view_func=entry_view, methods=["GET", "POST"])
entry_bp.add_url_rule("/<int:entry_id>", view_func=entry_view, methods=["GET", "PATCH", "DELETE"])

category_view = CategoryView.as_view("category_view")
category_bp = Blueprint("categories", __name__, url_prefix="/categories")
category_bp.add_url_rule("/", view_func=category_view, methods=["GET", "POST"])
category_bp.add_url_rule("/<int:category_id>", view_func=category_view, methods=["GET", "PATCH", "DELETE"])

article_view = ArticleView.as_view("article_view")
article_bp = Blueprint("articles", __name__, url_prefix="/categories/<int:category_id>/articles")
article_bp.add_url_rule("/", view_func=article_view, methods=["GET", "POST"])
article_bp.add_url_rule("/<int:article_id>", view_func=article_view, methods=["GET", "PATCH", "DELETE"])
