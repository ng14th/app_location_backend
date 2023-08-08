from flask import Blueprint
from src.user.db_login.views import route
from src.user.sso.sso_gmail.views import route as route_gmail
from src.user.sso.sso_facebook.views import route as route_facebook

# route = Blueprint('SSO', __name__, url_prefix='/sso')
# route.register_blueprint(route_gmail)          
# route.register_blueprint(route_facebook)