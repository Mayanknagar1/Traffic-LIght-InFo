from db import db

class TrafficLight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    light_color_work = db.Column(db.String(50), nullable=False)
    