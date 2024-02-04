from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Create the database tables
def db_init(app):
    db.init_app(app)
    # create the tables if the db doesnt already exist
    with app.app_context():
        db.create_all()