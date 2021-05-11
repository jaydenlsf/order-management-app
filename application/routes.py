from application import db, app
from flask import render_template, redirect, request, url_for, flash
from application.models import User, Order
from application.forms import UserForm
from sqlalchemy.exc import IntegrityError


@app.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route("/add-order", methods=["GET", "POST"])
def add_order():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                user = User(
                    email=form.email.data,
                    name=form.name.data,
                    house_number=form.house_number.data,
                    postcode=form.postcode.data,
                    phone=form.phone.data,
                )
                db.session.add(user)
                order = Order(
                    customer_id=User.query.filter_by(email=form.email.data).first().id
                )
                db.session.add(order)
                db.session.commit()
                return redirect(url_for("home"))
            except IntegrityError:
                flash("Please enter a different email address.")

    return render_template("add-order.html", title="Add Order", form=form)


@app.route("/update-order", methods=["GET", "POST"])
def update_order():
    return render_template("update-order.html", title="Update Order")
