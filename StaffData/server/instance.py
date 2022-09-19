from flask import Flask, Blueprint
from flask_restplus import Api

"""
Registration of all params that Flask app needs to build an RESTApi
    . Flask app params
    . Blueprint endpoints
    . Flask_restplus (Api and documentation) 
"""

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(
            self.app,
            version='1.0',
            title='StaffDataAPI',
            description='Provides all employees data',
            doc='/docs'
        )
        self.app.register_blueprint(self.blueprint)

        self.staff_ns = self.staffdata_ns()


    def staffdata_ns(self):
        return self.api.namespaces(name='StaffDataApi', path='/')


    def run(self):
        self.app.run(port=9000, debug=True)

server = Server()