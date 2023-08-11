# -*- coding: utf-8 -*-
from core.database.mongodb.mixins.mongodb_mixins import MongoCreateUpdateMixin
from core.database.mongodb.mongo import umongo_cnx
from umongo import fields, EmbeddedDocument

@umongo_cnx.register
class UserApp(MongoCreateUpdateMixin):
    region = fields.StringField(require = True)
    country = fields.StringField(require = True)
    username = fields.StringField(require = True)
    url_avatar = fields.StringField(allow_none = True, default="")
    information_mapping = fields.EmbeddedField('InformationMapping')
    
    class Meta:
        collection_name = "UserApp"

@umongo_cnx.register
class UserInformation(MongoCreateUpdateMixin):
    region = fields.StringField(require = True)
    country = fields.StringField(require = True)
    account_type = fields.StringField(require = True)
    username = fields.StringField(require = True)
    email = fields.StringField(require = True)
    password = fields.StringField(allow_none = True, default = "")
    token = fields.StringField(allow_none = True, default = "")
    active = fields.BooleanField(allow_none = True, default = True)
    
    class Meta:
        collection_name = "UserInformation"
        
@umongo_cnx.register
class InformationMapping(EmbeddedDocument):
    account_type = fields.StringField(allow_none=True)
    information_id = fields.ObjectIdField(require = True)
    email = fields.StringField(allow_none = True)
        
