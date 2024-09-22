from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///adogapet.db"
db.init_app(app)

@app.route("/")
def hello_world():
    return render_template("index.html")
