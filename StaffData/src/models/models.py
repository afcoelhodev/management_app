from flask_sqlalchemy import SQLAlchemy
from datetime import date

"""
Create the models that will be used to create tables on MySQL
    . SQL databases on local server using MySQL
"""

db = SQLAlchemy()

def config(app):
    db.init_app(app)
    app.db = db


class WorkersTable(db.Model):
    __tablename__ = 'workers'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    pos_level = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    salary = db.Column(db.Integer(), nullable=False)
    perf_ind = db.Column(db.String(20), nullable=False)


if __name__ == '__main__':
    db.create_all()
