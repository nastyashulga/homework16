import json

from flask import Flask
from app import db
from app.models import Offer, Order, User





def load_data(path):
    with open(path, encoding='UTF-8') as file:
        return json.load(file)

def load_orders(path):
    orders = load_data(path)
    for order in orders:

        db.session.add(
            Order(
                **order
            )
        )
        db.session.commit()

def load_offers(path):
    offers = load_data(path)
    for offer in offers:
        db.session.add(
            Offer(
                **offer
            )
        )
        db.session.commit()

def load_users(path):
    users = load_data(path)
    for user in users:
        db.session.add(
            User(
                **user
            )
        )
        db.session.commit()

def create_app():
    app = Flask(__name__)
    # Закидываем настройки, которые скоро использует алхимия
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False
    app.url_map.strict_slashes = False

    with app.app_context():
        db.init_app(app)
        db.create_all()
        offers = load_offers("/Users/nastiashulga/PycharmProjects/homework16/data/offers.json")
        orders = load_orders("/Users/nastiashulga/PycharmProjects/homework16/data/orders.json")
        users = load_users("/Users/nastiashulga/PycharmProjects/homework16/data/users.json")

    return app

app = create_app()