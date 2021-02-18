from flask import Flask


def create_app():
    # create and configure the app
    application = Flask(__name__)

    # A simple page that says hello
    @application.route('/hello')
    def hello():
        return 'Hello, World!'

    from app.health import context_blueprint
    application.register_blueprint(context_blueprint)

    return application
