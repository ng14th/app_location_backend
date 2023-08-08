from flask import Blueprint
from .db_login import route as route_db
route = Blueprint('DB-APP', __name__, url_prefix='/app')
route.register_blueprint(route_db)
