import json

from flask import request
from app.create_app import db, app
from app.models import User, Order, Offer


@app.route("/users", methods=['GET', 'POST'])
def get_users():
    result = []
    if request.method == 'GET':
        for user in User.query.all():
            result.append(user.return_data())

        return app.response_class(
            json.dumps(result),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'POST':

        data = request.json

        db.session.add(
            User(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

@app.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_user(id):
    result = []
    if request.method == 'GET':
        for user in User.query.filter(User.id == id).all():
            result.append(user.return_data())

        return app.response_class(
            json.dumps(result),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        try:
            user = db.session.query(User).get(id)
            user.id = data.get("id")
            user.first_name = data.first_name("first_name"),
            user.last_name = data.last_name("last_name"),
            user.age = data.age("age"),
            user.email = data.email("email"),
            user.role = data.get("role"),
            user.phone = data.phone("phone")
            db.session.commit()

        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'DELETE':
        try:
            db.session.query(User).filter(User.id == id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    result = []
    if request.method == 'GET':
        for order in Order.query.all():
            result.append(order.return_data())

        return app.response_class(
            json.dumps(result),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'POST':

        data = request.json

        db.session.add(
            Order(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

@app.route("/orders/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_order(id):
    result = []
    if request.method == 'GET':
        for order in Order.query.filter(Order.id == id).all():
            result.append(order.return_data())

        return app.response_class(
            json.dumps(result),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        try:
            order = db.session.query(Order).get(id)
            order.id = data.id("id"),
            order.name = data.name("name"),
            order.description = data.descriotion("description"),
            order.start_date = data.start_date("start_date"),
            order.end_date = data.end_date("end_date"),
            order.address = data.address("adress"),
            order.price = data.price("price"),
            db.session.commit()

        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'DELETE':
        try:
            db.session.query(Order).filter(Order.id == id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )


@app.route("/offers", methods=['GET', 'POST'])
def get_offers():
    result = []
    if request.method == 'GET':
        for offer in Offer.query.all():
            result.append(offer.return_data())

        return app.response_class(
            json.dumps(result),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'POST':

        data = request.json

        db.session.add(
            Offer(
                **data
            )
        )

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

@app.route("/offers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_offer(id):
    result = []
    if request.method == 'GET':
        for offer in Offer.query.filter(User.id == id).all():
            result.append(offer.return_data())

        return app.response_class(
            json.dumps(result),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'PUT':
        data = request.json
        try:
            offer = db.session.query(Offer).get(id)
            offer.id = data.id("id"),
            offer.order_id = data.order_id("id"),
            offer.executor_id = data.executor_id("id")
            db.session.commit()

        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )

    if request.method == 'DELETE':
        try:
            db.session.query(Offer).filter(Offer.id == id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
            ...

        return app.response_class(
            json.dumps("OK"),
            minetype="aplication/json",
            status=200
        )


if __name__ == '__main__':
    app.run("localhost", port=5037, debug=True)
