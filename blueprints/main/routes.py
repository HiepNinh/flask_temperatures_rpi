from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return "Hello World"


@main.route("/about")
def about():
    return "About page"
