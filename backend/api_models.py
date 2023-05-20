from flask_restx import fields
from datetime import datetime
from exts import api

# model (serializer)
user_model = api.model (
    "User",
    {
        "id":fields.Integer(),
        "name":fields.String(),
        "email":fields.String(),
        "password":fields.String()
    }
)

event_model = api.model (
    "Event",
    {
        "id":fields.Integer(),
        "title":fields.String(),
        "description":fields.String(),
        "time":fields.DateTime()
    }
)