from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    email = EmailField("Email address", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    house_number = StringField("House number", validators=[DataRequired()])
    postcode = StringField("Postcode", validators=[DataRequired()])
    phone = TelField("Phone number", validators=[DataRequired()])
    submit = SubmitField("Register")


class OrderForm(FlaskForm):
    email = EmailField("Email address", validators=[DataRequired()])
    submit = SubmitField("Place order")


class ChangeStatusForm(FlaskForm):
    status = SelectField(
        "Status",
        choices=[
            ("out for delivery", "Out for delivery"),
            ("cancel order", "Cancel order"),
        ],
    )
    submit = SubmitField("Change order status")
