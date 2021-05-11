from application import db
from datetime import datetime
import pytz


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    house_number = db.Column(db.String(12), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    order_numbers = db.Column(db.String(30), default="No order")


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    order_status = db.Column(db.String(30), default="Order placed")
    tracking_num = db.Column(db.String(12))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
