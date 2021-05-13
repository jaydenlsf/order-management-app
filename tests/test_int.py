from flask_testing import LiveServerTestCase
from selenium import webdriver
from application import app, db


class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_int.db"
        return app


def setUp(self):
    chrome_options = webdriver.chrome.Options()
    chrome_options.add_argument("--headless")

    self.driver = webdriver.Chrome(options=chrome_options)

    db.create_all()
    self.driver.get(f"http://localhost:5050/")


def tearDown(self):
    self.driver.quit()
    db.drop_all()
