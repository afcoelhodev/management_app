"""
Create and config all the endpoints through blueprints in Flask
    . Declaration of blueprints it's registered in /server/instance.py
    . Make querys to the workers_db and return filtered data
"""

from flask import Flask, jsonify
from StaffData.app import app
from ..database.workers_db import db, Workers
from ..models.models import WorkersTable

@app.route("/")
def home():
    return "Application running"


@app.route("/all_employees", methods=['GET'])
def get_all_data():
    dataset = db.query.all()
    result = []
    for item in dataset:
        result.append(item)

    return jsonify(result)


# @app.route("/create_db", methods=['GET'])
# def post_on_database():
#     with open("src/data.json", 'r') as file:
#         dataload = json.load(file)
#         for item in dataload:
#             db.staffdata.insert_one(item)
#
#     return jsonify(message="Registered with success")
