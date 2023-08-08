# -*- coding: utf-8 -*-
from flask import jsonify, make_response
from core.exceptions.reponse_exception import ErrorResponeException

# @app.errorhandler(ErrorResponeException)
def error_response_exception(exception: ErrorResponeException):
    error_response = {
        "success": exception.success,
        "data": exception.data,
        "length": exception.length,
        "error": exception.error,
        "error_code": exception.error_code
    }
    return make_response(jsonify(error_response), exception.status_code)

# @app.errorhandler(429)
def handle_rate_limit_exceeded(e):
    error_response = {
        "success" : False,
        "data" : [],
        "length" : 0,
        "error" : f"To many request, please try again later - {e.description}",
        "error_code" : 429
    }
    return make_response(jsonify(error_response), 429)

def handle_request_validator_error(e):
    msg = 'missing fields '
    for error in e.errors():
        field = f"{error.get('loc')[0]}, "
        msg = msg + field
    error_response = {
        "success" : False,
        "data" : [],
        "length" : 0,
        "error" : msg,
        "error_code" : 400
    }
    return make_response(jsonify(error_response), 400)