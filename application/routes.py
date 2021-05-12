from application import db, app
from flask import render_template, redirect, request, url_for, flash
from application.models import Users, Orders
from application.forms import (
    UserForm,
    OrderForm,
    ChangeStatusForm,
)
from application.tracking_gen import tracking_gen
from datetime import datetime
import pytz


def pad_num(num):
    return f"{num:>04}"


@app.route("/")
def home():
    users = Users.query.all()
    orders = Orders.query.all()
    order_placed = []
    out_for_delivery = []
    delivered = []

    for order in orders:
        if order.order_status == "order placed":
            order_placed.append(order)
        elif order.order_status == "out for delivery":
            out_for_delivery.append(order)
        elif order.order_status == "delivered":
            delivered.append(order)
    order_count = len(order_placed) + len(out_for_delivery) + len(delivered)
    return render_template(
        "index.html",
        users=users,
        orders=orders,
        order_placed=order_placed,
        out_for_delivery=out_for_delivery,
        delivered=delivered,
        order_count=order_count,
        pad_num=pad_num,
    )


@app.route("/add-Orders", methods=["GET", "POST"])
def add_order():
    form = OrderForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user is None:
                flash("Account does not exist.")
                # return redirect(url_for("register"))
            elif user is not None:
                new_order = Orders(
                    customer_id=user.id,
                    date=datetime.now(pytz.timezone("Europe/London")).date(),
                    time=datetime.now(pytz.timezone("Europe/London"))
                    .replace(microsecond=0)
                    .time(),
                )
                db.session.add(new_order)
                db.session.commit()
                user_order = (
                    Orders.query.filter_by(customer_id=user.id)
                    .order_by(Orders.id.desc())
                    .first()
                    .id
                )
                if user.order_numbers == "no order":
                    user.order_numbers = user_order
                    db.session.commit()
                else:
                    user.order_numbers = str(user.order_numbers)
                    user.order_numbers += ", " + str(user_order)
                    db.session.commit()
                flash(f"New order has been placed by {user.name}.")
                # return redirect(url_for("home"))

    return render_template("add-order.html", form=form)


@app.route("/view-order/<int:id>", methods=["GET", "POST"])
def view_order(id):
    order = Orders.query.filter_by(id=id).first()
    return render_template("view-order.html", order=order, pad_num=pad_num)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user is None:
                new_user = Users(
                    email=form.email.data,
                    name=form.name.data,
                    house_number=form.house_number.data,
                    postcode=form.postcode.data,
                    phone=form.phone.data,
                )
                db.session.add(new_user)
                db.session.commit()
                flash("Successfully registered a new user.")
            else:
                flash("Please use a different email.")
                return redirect(url_for("register"))

    return render_template("register.html", title="Register", form=form)


@app.route("/update-order/<int:id>", methods=["GET", "POST"])
def update_order(id):
    form = ChangeStatusForm()
    tracking_numbers = []
    orders = Orders.query.all()
    for order in orders:
        if order.tracking_num != None:
            tracking_numbers.append(order.tracking_num)

    if request.method == "POST":
        update_order = Orders.query.filter_by(id=id).first()
        if form.validate_on_submit():
            update_order.order_status = form.status.data
            db.session.commit()
            if update_order.order_status == "out for delivery":
                if update_order.tracking_num in tracking_numbers:
                    update_order.tracking_num = tracking_gen()
                else:
                    update_order.tracking_num = tracking_gen()
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("update-order.html", form=form, update_order=update_order)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    delete_order = Orders.query.filter_by(id=id).first()
    db.session.delete(delete_order)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delivered/<int:id>", methods=["POST"])
def delivered(id):
    delivered_order = Orders.query.filter_by(id=id).first()
    delivered_order.order_status = "delivered"
    db.session.commit()
    return redirect(url_for("home"))
