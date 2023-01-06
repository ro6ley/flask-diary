from datetime import datetime

from app import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    articles = db.relationship("Article", back_populates="category", cascade="all, delete-orphan")
    # owner

    def __repr__(self) -> str:
        return f"<Category - {self.name}>"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))
    url = db.Column(db.String())
    read_status = db.Column(db.Boolean, default=False, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship("Category", back_populates="articles", foreign_keys='Article.category_id')
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # owner

    def __repr__(self) -> str:
        return f"<Article - {self.title}>"

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

