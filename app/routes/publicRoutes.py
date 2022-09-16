from flask import Blueprint, render_template
from app.controllers.errorController import catchError

publicRoutes = Blueprint('publicRoutes', __name__)

@publicRoutes.route('/', methods=["GET"])
@catchError()
def index():
    return render_template('public/index.html')

@publicRoutes.errorhandler(404)
def page_not_found(error):
    return render_template('public/error.html', error)

