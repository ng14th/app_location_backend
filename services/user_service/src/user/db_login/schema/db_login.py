from pydantic import BaseModel, EmailStr, root_validator
from typing import *
import re
from core.exceptions.handler_exception import ErrorResponeException
from core.exceptions.mapping_exception import get_error_code

class LoginSchema(BaseModel):
    pass


class RegisterSchema(BaseModel):
    email : str
    username : str
    password : str
    retype_password : str
    country : str
    region : str
    agree_terms : bool
    
    @root_validator()
    def validator_retype_password(cls, v):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', v.get('email')):
            raise ErrorResponeException(**get_error_code(1003))
        if v.get('password') != v.get('retype_password'):
            raise ErrorResponeException(**get_error_code(2002))
        return v
            
class LoginSchema(BaseModel):
    username_email : str
    password : str
    remember : bool