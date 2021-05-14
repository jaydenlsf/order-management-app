from flask_testing import LiveServerTestCase
from selenium import webdriver
import unittest
from application import app, db
from urllib.request import urlopen
from flask import url_for


class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test_int.db",
            SECRET_KEY="secretkey",
            LIVESERVER_PORT=self.TEST_PORT,
            DEBUG=True,
            Testing=True,
        )
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all()
        self.driver.get(f"http://localhost:{self.TEST_PORT}")

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f"http://localhost:{self.TEST_PORT}")
        self.assertEqual(response.code, 200)


class TestCreateUser(TestBase):
    def test_submit_input(self):
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(
            "test@gmail.com"
        )
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys("Test")
        self.driver.find_element_by_xpath('//*[@id="house_number"]').send_keys("8")
        self.driver.find_element_by_xpath('//*[@id="postcode"]').send_keys("G3 8PX")
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys("07999999999")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
