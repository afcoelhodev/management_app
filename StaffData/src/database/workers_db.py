from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from StaffData.app import app

"""
Create a connection to PostgresDB through OOP class
    . Create table if first access
    . Add new row using /database/employee_gen.py
"""

db = SQLAlchemy(app)


class Workers(db.Model):
    def __init__(self):

        POSTGRES = {
            'user': 'postgres',
            'password': 'workers_info123',
            'db': "workers_info",
            'host': 'localhost',
            'port': '5432',
        }

 # POSTGRES = {
 #            'user': 'Manager',
 #            'password': 'postgres123',
 #            'db': "",
 #            'host': 'localhost',
 #            'port': '5432',
 #        }