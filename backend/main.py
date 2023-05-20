from flask import Flask,request
from flask_restx import Api,Resource,fields
from config import DevConfig
from flask_migrate import Migrate
from exts import db,api
from models import User,Event
# from flask_cors import CORS

from users import user_ns
from events import event_ns


app = Flask(__name__)
app.config.from_object(DevConfig)

### allows api to work with app running on different port ###
# CORS(app)

db.init_app(app)
migrate = Migrate(app,db,compare_type=True)
# api = Api(app, doc='/docs')
# api=Api(app,doc='/docs')
api.init_app(app, docs='/docs')
api.add_namespace(user_ns)
api.add_namespace(event_ns)

@app.shell_context_processor
def make_shell_context():
    return {
        "db":db,
        "User":User,
        "Event":Event
    }




# Testing API
@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return{"message":"Hello World"}
    

if __name__ == "__main__":
    app.run()