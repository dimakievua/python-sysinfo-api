from flask import Flask, render_template
from . import printinfo
import json
import os

obj1 = printinfo.SysInfo("gb")

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    obj1 = printinfo.SysInfo("gb")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        var = json.loads(obj1.displayInfo())
        return render_template('index.html', **locals())

    @app.route('/healthcheck')
    def healthcheck():
        return "Ok"

    @app.route("/api/all")
    def all():
        return obj1.displayInfo()

    #del obj1
    return app
