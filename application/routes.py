from application import db, app
from flask import render_template, redirect, request, url_for, flash
from application.models import User, Order
from application.forms import UserForm, OrderForm
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import pytz


@app.route("/")
def home():
    users = User.query.all()
    orders = Order.query.all()
    return render_template("index.html", users=users, orders=orders)


@app.route("/add-order", methods=["GET", "POST"])
def add_order():
    form = OrderForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None:
                return redirect(url_for("register"))
            elif user is not None:
                new_order = Order(
                    customer_id=user.id,
                    date=datetime.now(pytz.timezone("Europe/London")).date(),
                    time=datetime.now(pytz.timezone("Europe/London")).time(),
                )
                db.session.add(new_order)
                db.session.commit()
                user_order = (
                    Order.query.filter_by(customer_id=user.id)
                    .order_by(Order.id.desc())
                    .first()
                    .id
                )
                if user.order_numbers == "No order":
                    user.order_numbers = user_order
                    db.session.commit()
                else:
                    user.order_numbers = str(user.order_numbers)
                    user.order_numbers += ", " + str(user_order)
                    db.session.commit()
                return redirect(url_for("home"))

    return render_template("add-order.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None:
                new_user = User(
                    email=form.email.data,
                    name=form.name.data,
                    house_number=form.house_number.data,
                    postcode=form.postcode.data,
                    phone=form.phone.data,
                )
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("home"))
            else:
                flash("Please use a different email.")
                return redirect(url_for("register"))

    return render_template("register.html", title="Register", form=form)


@app.route("/update-order", methods=["GET", "POST"])
def update_order():
    return render_template("update-order.html", title="Update Order")
