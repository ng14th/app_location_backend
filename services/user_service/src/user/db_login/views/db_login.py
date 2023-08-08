# -*- coding: utf-8 -*-
from flask import Blueprint, request
from core.schema.api_respone import custom_respone
from src.user.db_login.utils.db_login import register_user_mongodb
route = Blueprint("login-db", __name__)

@route.post('/test-connect-app')
async def test_connect_facebook():
    return {}


@route.post('/register-user')
async def test_mongo():
    result = await register_user_mongodb(request.get_json())
    if result:
        return custom_respone({
            "data" : [result]
        })
    return custom_respone({
        "data" : [],
        "success" : False
    })    