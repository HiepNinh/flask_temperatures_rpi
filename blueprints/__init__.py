from blueprints.main.routes import main
from blueprints.lab_temp.routes import lab_temp
from blueprints.error.routes import errors

def regist_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(lab_temp)
    app.register_blueprint(errors)