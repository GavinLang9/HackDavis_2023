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
        "name":fields.String(),
        "description":fields.String(),
        "items":fields.String(),
        "start_time":fields.DateTime(),
        "end_time":fields.DateTime(),
        "address":fields.String(),
        "contact":fields.String(),
        "notes":fields.String(),
        "website":fields.String()
    }
)

# time_model =api.model (
#     "Time",
#     {
#         "id":fields.Integer(),
#         "start_time":fields.DateTime(),
#         "end_time":fields.DateTime()
#     }
# )