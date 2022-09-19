import json
from flask import Flask, request, jsonify
# from StaffData.server.instance import server
# from StaffData.src.models.workers_db import Workers
from StaffData.src.models.models import db
from .src.endpoints import staffdata
from .server.instance import server

# api = server.api
# app = server.app


app = Flask(__name__)

app.config.from_pyfile('congif.py')

# importar os endpoints do staffdata


if __name__ == '__main__':
    app.run(port=9000, debug=True)
    # db.init_app(app)
    # server.run()
