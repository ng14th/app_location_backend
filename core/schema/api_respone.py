# -*- coding: utf-8 -*-
from typing import List, Any
from pydantic import BaseModel
from flask import jsonify, make_response

class ApiResponseSchema(BaseModel):
    success : bool = True
    data : List[Any] = []
    length : int = 0
    error : str = ""
    error_code : int = 0
    status_code : int = 200


def custom_respone(data):    
    respone_data = ApiResponseSchema.parse_obj(data)
    error_response = {
        "success": respone_data.success,
        "data": respone_data.data,
        "length": respone_data.length,
        "error": respone_data.error,
        "error_code": respone_data.error_code
    }
    response = make_response(jsonify(error_response), respone_data.status_code)
    return response