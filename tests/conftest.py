from datetime import datetime
import pytest

from app import create_app, db
from app.models import Article, Category, Entry


@pytest.fixture()
def app():
    app = create_app(environment='testing')
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def init_db(app):
    with app.app_context():
        db.create_all()

        # test entries
        entry1 = Entry(title="Test title 1", content="Test content 1", created_at=datetime.utcnow())
        db.session.add(entry1)

        entry2 = Entry(title="Test title 2", content="Test content 2", created_at=datetime.utcnow())
        db.session.add(entry2)

        # test categories
        category1 = Category(name="Test category 1", created_at=datetime.utcnow(),
                                description="Test description 1")
        db.session.add(category1)

        category2 = Category(name="Test category 2", created_at=datetime.utcnow(),
                                description="Test description 2")
        db.session.add(category2)

        db.session.commit()

        # test articles
        article1 = Article(category_id=category1.id, title="Test article 1", url="google.com",
                            description="Test description 1", created_at=datetime.utcnow())
        db.session.add(article1)

        article2 = Article(category_id=category2.id, title="Test category 2", url="bing.com",
                            description="Test article 2", created_at=datetime.utcnow())
        db.session.add(article2)

        db.session.commit()

        yield db

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
