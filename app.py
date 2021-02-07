from flask import Flask
from blueprints import regist_blueprints


app = Flask(__name__)

regist_blueprints(app)
