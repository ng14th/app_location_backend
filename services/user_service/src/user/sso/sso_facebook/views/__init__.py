from flask import Blueprint
from .login import route as route_login_facebook

route = Blueprint('SSO-facebook', __name__ , url_prefix='/facebook')
route.register_blueprint(route_login_facebook)