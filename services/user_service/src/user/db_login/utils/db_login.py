# -*- coding: utf-8 -*-
from src.user.db_login.schema.db_login import RegisterSchema, LoginSchema
from src.user.models.user_models import UserInformation
from core.exceptions.handler_exception import ErrorResponeException
from core.exceptions.mapping_exception import get_error_code
from src.tools.generator_token import hass_password

async def register_user_mongodb(data):
    request_data = RegisterSchema.parse_obj(data)
    try:
        check_user_existed = await UserInformation.find_one({
            "region" : request_data.region,
            "country" : request_data.country,
            "email" : request_data.email
        })
        if check_user_existed:
            raise ErrorResponeException(**get_error_code(1001))
        
        check_username = await UserInformation.find_one({
            "region" : request_data.region,
            "country" : request_data.country,
            "username" : request_data.username
        })
        if check_username:
            raise ErrorResponeException(**get_error_code(1002))
        password = hass_password(request_data.password)
        new_user = UserInformation(
            region=request_data.region,
            country=request_data.country,
            account_type='APP',
            username=request_data.username,
            email=request_data.email,
            password=str(password),
            active=False
        )
        await new_user.commit()
        if new_user:
            return {
                "username" : request_data.username,
                "email" : request_data.email
            }
        else:
            raise ErrorResponeException(**get_error_code(1004))
    except ErrorResponeException as er:
        raise er
    except Exception as e:
        raise e
    
    