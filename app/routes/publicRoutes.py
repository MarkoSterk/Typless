from flask import Blueprint, render_template
from app.controllers.errorController import catchError

publicRoutes = Blueprint('publicRoutes', __name__)

#index/main page endpoint. Returns html response
@publicRoutes.route('/', methods=["GET"])
@catchError()
def index():
    return render_template('public/index.html')



