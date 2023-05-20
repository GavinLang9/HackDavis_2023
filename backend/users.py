from flask_restx import Api, Resource, Namespace
from models import User
from flask import request

from api_models import user_model
from exts import api 

user_ns = Namespace('user', description="A namespace for Users")

@user_ns.route('/users')
class UsersResource(Resource):

    @user_ns.marshal_list_with(user_model)
    def get(self):
        """Get all users"""

        users = User.query.all()

        return users
    
    @user_ns.marshal_with(user_model)
    @user_ns.expect(user_model)
    def post(self):
        """Create a new user"""
        data = request.get_json()

        new_user = User(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password')
        )

        new_user.save()

        return new_user,201

@user_ns.route('/user/<int:id>')
class UserResource(Resource):
    @user_ns.marshal_with(user_model)
    def get(self,id):
        """Get a user by id"""
        user=User.query.get_or_404(id)

        return user
    
    @user_ns.marshal_with(user_model)
    def post(self,id):
        """Update a user by id"""
        data = request.get_json()
        
        password = data.get("password")
        user = User.query.get_or_404(id)
        user.update(user.name, user.email, password)

        return user,201
    
    @user_ns.marshal_with(user_model)
    def delete(self,id):
        """Delete a user by id"""
        user_to_delete = User.query.get_or_404(id)
        user_to_delete.delete()