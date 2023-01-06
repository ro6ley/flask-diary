from datetime import datetime
from flask import views, jsonify, make_response, abort, request

from app.models import Article, Category
from app import db


class CategoryView(views.MethodView):
    def get(self, category_id=None):
        """List all categories or return the category matching the ID provided """
        if not category_id:
            # TODO: pagination
            categories = [c.to_dict() for c in Category.query.all()]
            return make_response(jsonify(categories), 200)
        else:
            category = db.session.get(Category, category_id)
            if not category:
                return abort(404)
            return make_response(jsonify(category.to_dict()), 200)

    def post(self):
        """ Create a single category """
        request_data = request.get_json()

        if not request_data.get("name"):
            return abort(400)

        new_category = Category(name=request_data.get("name"), description=request_data.get("description"), created_at=datetime.utcnow())
        db.session.add(new_category)
        db.session.commit()

        return make_response(jsonify(new_category.to_dict()), 200)


    def patch(self, category_id):
        """ Update a single category """
        category = db.session.get(Category, category_id)
        if not category:
            return abort(404)

        category.name = request.get_json().get("name", category.name)
        category.description = request.get_json().get("description", category.description)
        db.session.commit()

        return make_response(jsonify(category.to_dict()), 200)


    def delete(self, category_id):
        """ Delete a single category """
        category = db.session.get(Category, category_id)
        if not category:
            return abort(404)

        db.session.delete(category)
        db.session.commit()

        return make_response(jsonify(category.to_dict()), 204)


class ArticleView(views.MethodView):
    def get(self, category_id=None, article_id=None):
        """List all diary articles or return the article matching the ID provided """
        if not article_id:
            # TODO: pagination
            articles = [a.to_dict() for a in Article.query.all()]
            return make_response(jsonify(articles), 200)
        else:
            article = db.session.get(Article, article_id)
            if not article:
                return abort(404)
            return make_response(jsonify(article.to_dict()), 200)

    def post(self, category_id):
        """ Create a single article """
        request_data = request.get_json()

        if not request_data.get("title"):
            return abort(400)

        new_article = Article(title=request_data.get("title"),
                              description=request_data.get("description"),
                              url=request_data.get("url"),
                              read_status=False,
                              category_id=category_id,
                              created_at=datetime.utcnow())
        db.session.add(new_article)
        db.session.commit()

        return make_response(jsonify(new_article.to_dict()), 200)


    def patch(self, category_id, article_id):
        """ Update a single article """
        article = db.session.get(Article, article_id)
        if not article:
            return abort(404)

        article.title = request.get_json().get("title", article.title)
        article.description = request.get_json().get("description", article.description)
        article.url = request.get_json().get("url", article.description)
        article.read_status = request.get_json().get("read_status", article.description)
        db.session.commit()

        return make_response(jsonify(article.to_dict()), 200)


    def delete(self, category_id, article_id):
        """ Delete a single article """
        article = db.session.get(Article, article_id)
        if not article:
            return abort(404)

        db.session.delete(article)
        db.session.commit()

        return make_response(jsonify(article.to_dict()), 204)
