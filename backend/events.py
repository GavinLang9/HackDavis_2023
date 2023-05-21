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
            name=data.get('name'),
            description=data.get('description'),
            items=data.get('items'),
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            address=data.get('address'),
            contact=data.get('contact'),
            notes=data.get('notes'),
            website=data.get('website')

        )

        new_event.save()

        return new_event, 201
    


@event_ns.route("/event")
class EventsResource(Resource):

    @event_ns.marshal_list_with(event_model)
    def get(self):
        """Get a event"""
        data = request.get_json()
        ID = data.get('id')
        events = Event.query.filter_by(id=ID)

        return events
    
    @event_ns.marshal_with(event_model)
    @event_ns.expect(event_model)
    def post(self):
        """edit event"""
        data = request.get_json()

        new_event = Event (
            name=data.get('name'),
            description=data.get('description'),
            items=data.get('items'),
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            address=data.get('address'),
            contact=data.get('contact'),
            notes=data.get('notes'),
            website=data.get('website')

        )

        new_event.save()

        return new_event, 201
    
    @event_ns.marshal_with(event_model)
    def delete(self):
        """Delete a event by id"""
        data = request.get_json()
        id = data["id"]

        event_to_delete = Event.query.get_or_404(id)
        event_to_delete.delete()

@event_ns.route("/getRecents")
class EventsResource(Resource):

    @event_ns.marshal_list_with(event_model)
    def get(self):
        """Get recent Events"""
        
        
        events = Event.query.order_by(Event.start_time).all()

        return events
    
    @event_ns.marshal_with(event_model)
    @event_ns.expect(event_model)
    def post(self):
        """Create new event"""
        data = request.get_json()

        new_event = Event (
            name=data.get('name'),
            description=data.get('description'),
            items=data.get('items'),
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            address=data.get('address'),
            contact=data.get('contact'),
            notes=data.get('notes'),
            website=data.get('website')
        )

        new_event.save()

        return new_event, 201