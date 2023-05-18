import api.controllers.user as controller
from flask import current_app as app
from flask_restful import Api

api = Api(app)

api.add_resource(controller.AddUser, '/add-user')
api.add_resource(controller.GetUsers, '/get-users')
api.add_resource(controller.DeleteUser, '/delete-user')