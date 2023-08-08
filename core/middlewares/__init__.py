# from flask_middleware import Middleware
resource_cors = {
    r"/*": {
        "origins": "http://localhost:8*", 
        "methods": "POST", 
        "headers": "Content-Type, *"
        }
}