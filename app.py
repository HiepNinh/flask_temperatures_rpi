from flask import Flask
from blueprints import regist_blueprints


app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

regist_blueprints(app)
