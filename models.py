from flask_sqlalchemy import SQLAlchemy
from flask import session

db = SQLAlchemy()

class Discounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    percentage = db.Column(db.Float, nullable=False)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)
