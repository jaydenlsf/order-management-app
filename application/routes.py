from application import db, app


@app.route("/")
def home():
    return "Welcome to the homepage."
