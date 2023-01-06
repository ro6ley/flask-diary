from flask import render_template

from app.routes import root_bp


@root_bp.route('/', methods=('GET',))
def index():
    return render_template("index.html")
