import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)

import os

from flask_dance.contrib.google import make_google_blueprint, google

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'


blueprint = make_google_blueprint(
    client_id="369592527252-ja2o5jgmi8og256en5kjdje7bp8cdhiu.apps.googleusercontent.com",
    client_secret="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",
    # reprompt_consent=True,
    offline=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")



app.config['SECRET_KEY'] = 'mykey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)



login_manager.init_app(app)
login_manager.login_view = "login"