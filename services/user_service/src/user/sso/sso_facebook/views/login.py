# -*- coding: utf-8 -*-
from flask import Blueprint
route = Blueprint("login-facebook", __name__)

@route.post('/test-connect-facebook')
async def test_connect_facebook():
    return {}