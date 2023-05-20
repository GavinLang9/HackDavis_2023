from flask_restx import Api, Resource, Namespace
from models import Event
from flask import request

from api_models import event_model
from exts import api 

event_ns = Namespace('event', description="A namespace for the events")

@event_ns.route("/events")
class EventsResource(Resource):

    @event_ns.marshal_list_with(event_model)
    def get(self):
        """Get all events"""

        events = Event.query.all()

        return events
    
    @event_ns.marshal_with(event_model)
    @event_ns.expect(event_model)
    def post(self):
        """Create new event"""
        data = request.get_json()

        new_event = Event (
            title=data.get('title'),
            description=data.get('description'),
            time=data.get('time')
        )

        new_event.save()

        return new_event, 201