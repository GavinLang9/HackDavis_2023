import json
from flask import Flask
from flask_restx import Resource
from api_models import event_model
from flask import request
from events import Event
import re
import datetime
from main import app
from events import event_ns
# Load data from the JSON file
with open("food_banks.json") as file:
    data = json.load(file)

# Iterate over each food bank in the list
for bank in data:
    # Extract information and assign to variables
    name = bank["Name"]
    items = bank["Items Available"]
    address = bank["Address"]
    contact = bank["Contact"]
    notes = bank["Notes"]
    website = bank["Website"]
    start_time = datetime.datetime.strptime(bank["Start_times"][0], "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(bank["End_times"][0], "%Y-%m-%d %H:%M:%S")

    event = Event(
        name=name,
        description='',
        items=items,
        start_time=start_time,
        end_time=end_time,
        address=address,
        contact=contact,
        notes=notes,
        website=website
    )
    event.save()


@event_ns.route("/events")
class EventsResource(Resource):
    
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
    
# with open('./data.json') as jsonfile:
#     data = json.load(jsonfile)
#     print(data)
#     for item in data:
#         days = item['days']
#         print(days)
#         time = item['Hours'].split(',')
#         for i in range(0,len(time)-1):
#             time[i] = time[i].split('-')
#             startTime = time[i][0]
#             datetime_str = f"{days[i]} {startTime}:00"
#             datetime_object = datetime.strptime(datetime_str, '%m-%d-%y %H:%M:%S')
#             print(datetime_object)
        # days = item['days'].split(',')
        # print(days)
        # datetime = 
        # event = Event(
        #     name=item['Name'],
        #     items=item['Items Available'],

        #     )

        # data = json

        # for item in data:
        #     name = item["name"]
        #     description = item[]