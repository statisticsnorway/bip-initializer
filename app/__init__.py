from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics.for_app_factory()


def create_app():
    # create and configure the app
    application = Flask(__name__)

    # Initialize metric library
    metrics.init_app(application)

    # A simple page that says hello
    @application.route('/hello')
    def hello():
        return 'Hello, World!'

    from app.health import context_blueprint
    application.register_blueprint(context_blueprint)

    return application
