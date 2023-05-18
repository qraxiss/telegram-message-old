from flask_restful import Resource, request
import logic.models.user as user

from errors.handler import handler
    
class GetUsers(Resource):
    @handler
    def get(self):
        return user.get_users(request.json)

class DeleteUser(Resource):
    @handler
    def delete(self):
        return user.delete_user(request.json)
    
class AddUser(Resource):
    @handler
    def post(self):
        return user.add_user(request.json)