from flask import Flask, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_CONFIG']) # export APP_CONFIG="config.Dev"
db = SQLAlchemy(app)
app.secret_key = 'development'

from octy import linkedinAuth

if __name__ == '__main__':
    app.run()