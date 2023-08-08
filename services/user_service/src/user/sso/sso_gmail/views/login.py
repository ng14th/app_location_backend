# -*- coding: utf-8 -*-
from flask import Blueprint, request
from core.schema.api_respone import custom_respone
route = Blueprint("login-gmail", __name__)

@route.post('/test-connect-gmail')
async def test_connect_facebook():
    return {}