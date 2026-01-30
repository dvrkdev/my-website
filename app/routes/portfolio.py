from flask import Blueprint

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/')
def index():
    return '<h1>Portfolio!</h1>'