# -*- coding: utf-8 -*-
ERROR_CODE = {
    1000: ("User not exist in system", 401),
    1001: ("Email is existed in system", 422),
    1002: ("Username is existed", 422),
    1003: ("Email is wrong format", 400),
    1004: ("Register fail", 422),
    2002: ("Retype password must be match with password", 422),
    2003: ("Password is not correct", 401),
    99400: ("Missing fields {values}", 400),
    99401: ("Invalid token", 401),
    99403: ("Token expired", 403),
    98403: ("Could not validate credentials", 403),
}


def get_error_code(error_code: int, data: str = None):
    if data:
        error_detail = ERROR_CODE.get(error_code, "Error code is not define")[0].replace('{values}', data)
    else:
        error_detail = ERROR_CODE.get(error_code, "Error code is not define")[0]
    status_code = ERROR_CODE.get(error_code, "Error code is not define")[1] if ERROR_CODE.get(error_code, "Error code is not define") else 200

    return {
        "success" : False,
        "error_code" : error_code,
        "error" : error_detail,
        "status_code" : status_code
    }