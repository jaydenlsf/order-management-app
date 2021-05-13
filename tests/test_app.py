from application.routes import pad_num, tracking_gen
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Users, Orders
from os import getenv


class TestCase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="TEST_SECRET_KEY",
            DEBUG=True,
            WTF_CSRF_ENABLED=False,
        )
        return app

    def setUp(self):
        db.create_all()

        new_user = Users(
            email="test@gmail.com",
            name="Test",
            house_number="8",
            postcode="G3 8PX",
            phone="07999999999",
        )
        db.session.add(new_user)

        new_order = Orders(customer_id=1)
        db.session.add(new_order)

        new_order = Orders(customer_id=1, order_status="out for delivery")
        db.session.add(new_order)

        new_order = Orders(customer_id=1, order_status="delivered")
        db.session.add(new_order)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestPadNum(TestCase):
    def test_pad_num(self):
        self.assertEqual(len(pad_num(3)), 4)


class TestTrackingGen(TestCase):
    def test_tracking_gen(self):
        self.assertEqual(len(tracking_gen()), 8)


class TestViews(TestCase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)

    def test_add_order_get(self):
        response = self.client.get(url_for("add_order"))
        self.assertEqual(response.status_code, 200)

    def test_view_order_get(self):
        response = self.client.get(url_for("view_order", id=1))
        self.assertEqual(response.status_code, 200)

    def test_register_get(self):
        response = self.client.get(url_for("register"))
        self.assertEqual(response.status_code, 200)

    def test_update_order_get(self):
        response = self.client.get(url_for("update_order", id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for("delete", id=1))
        self.assertEqual(response.status_code, 405)

    def test_delivered_get(self):
        response = self.client.get(url_for("delivered", id=1))
        self.assertEqual(response.status_code, 405)


class TestCreateUser(TestCase):
    def test_create_user(self):
        response = self.client.post(
            url_for("register"),
            data=dict(
                email="test2@gmail.com",
                name="Test2",
                house_number="82",
                postcode="G2 8PX",
                phone="0788888888",
            ),
            follow_redirects=True,
        )
        user = Users.query.filter_by(id=2).first()
        self.assertEqual("test2@gmail.com", user.email)
        self.assertEqual("Test2", user.name)
        self.assertEqual("82", user.house_number)
        self.assertEqual("G2 8PX", user.postcode)
        self.assertEqual("0788888888", user.phone)


class TestDuplicateEmail(TestCase):
    def test_duplicate_email(self):
        response = self.client.post(
            url_for("register"),
            data=dict(
                email="test@gmail.com",
                name="Test",
                house_number="82",
                postcode="G2 8PX",
                phone="0788888888",
            ),
            follow_redirects=True,
        )


class TestAddOrder(TestCase):
    def test_add_order(self):
        response = self.client.post(
            url_for("add_order", id=1),
            data=dict(email="test@gmail.com"),
            follow_redirects=True,
        )
        order = Orders.query.filter_by(id=1).first()
        user = Users.query.filter_by(id=1).first()
        self.assertEqual(1, order.customer_id)
        self.assertEqual("order placed", order.order_status)
        self.assertEqual(None, order.tracking_num)
        self.assertIn(order, user.orders)


class TestAddOrderNoUser(TestCase):
    def test_add_order_no_user(self):
        response = self.client.post(
            url_for("add_order"), data=dict(email="nonexistingemail@gmail.com")
        )


class TestViewOrder(TestCase):
    def test_view_order(self):
        response = self.client.get(
            url_for("view_order", id=1),
            data=dict(
                id="0006",
                name="Test",
                house_number="8",
                postode="G3 8PX",
                phone="07999999999",
            ),
        )
        self.assertIn(b"0001", response.data)
        self.assertIn(b"Test", response.data)
        self.assertIn(b"8", response.data)
        self.assertIn(b"G3 8PX", response.data)
        self.assertIn(b"07999999999", response.data)


class TestUpdateOrder(TestCase):
    def test_update_order(self):
        response = self.client.post(
            url_for("update_order", id=1),
            data=dict(
                status="out for delivery",
                tracking_num_len=8,
            ),
        )
        order = Orders.query.filter_by(id=1).first()
        self.assertEqual("out for delivery", order.order_status)
        self.assertEqual(len(order.tracking_num), 8)


class TestDelivered(TestCase):
    def test_delivered(self):
        response = self.client.post(url_for("delivered", id=1))
        order = Orders.query.filter_by(id=1).first()
        self.assertEqual("delivered", order.order_status)


class TestDelete(TestCase):
    def test_delete(self):
        response = self.client.post(url_for("delete", id=1))
        order = Orders.query.filter_by(id=1).first()
        self.assertEqual(order, None)
