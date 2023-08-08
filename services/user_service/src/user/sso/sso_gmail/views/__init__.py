from flask import Blueprint
from .login import route as route_login_gmail
route = Blueprint('SSO-Gmail', __name__, url_prefix='/gmail')
route.register_blueprint(route_login_gmail)
