from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mmesa.db"
db.init_app(app)

from mmesa import routes