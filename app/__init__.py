# -*- coding: utf-8 -*-

"""
    DODOA
        A better OA system for Design Management.
    
    :Author:    Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :Time:      2019-02-19 22:09
    :copyright: © 2019 Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :license:   GPL v3, see LICENSE for more details.
"""

import os

from flask import Flask

from app.config import config


def create_app(config_name=None):
    """
    Create the Flask app via Factory pattern.
    :param config_name:
    :return: the Flask app object.
    """
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    # register_errors(app)
    register_commands(app)
    register_shell_context(app)
    # register_template_context(app)
    # register_request_handlers(app)
    return app
