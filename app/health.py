from datetime import datetime

from flask import Blueprint, g, make_response, render_template

context_blueprint = Blueprint('context', __name__)


@context_blueprint.before_app_request
def load_context_info():
    g.appname = 'BIP Initializer'
    g.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')


def create_json_response():
    response = make_response(render_template('context.json'))
    response.headers['Content-Type'] = 'application/json'
    return response


# Liveness endpoint
@context_blueprint.route('/health/alive')
def alive():
    g.status = 'Not dead!'
    return create_json_response()


# Readiness endpoint
@context_blueprint.route('/health/ready')
def ready():
    g.status = "I'm ready!"
    return create_json_response()
