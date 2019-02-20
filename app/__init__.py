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

import click
from flask import Flask

from app.config import config
from app.extensions import db, moment, migrate
from app.models import Gender, Employee, Project
from app.views import bp as bp_main


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

    # register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    # register_errors(app)
    register_commands(app)
    # register_shell_context(app)
    # register_template_context(app)
    # register_request_handlers(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)


def register_blueprints(app):
    app.register_blueprint(bp_main)


def register_commands(app):
    @app.cli.command('init')
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def db_init(drop):
        """
        Initialize the database of the Flask application.
        Create the tables, and fill some basic data.
        :return: None.
        """
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            click.echo('Dropping tables...')
            db.drop_all()
            click.echo('Dropped.')

        click.echo('Creating database...')
        db.create_all()
        click.echo('Created.')

        click.echo('Filling basic data...')
        # Data for class Gender().
        db.session.add_all([
            Gender(name='Unknown', name_zh='未知'),
            Gender(name='Male', name_zh='男性'),
            Gender(name='Female', name_zh='女性'),
        ])

        # Data for class Company().
        db.session.add_all([
            Project(name='南京2016G61地块项目', code='海珀'),
            Project(name='南京2017G41地块项目', code='海悦'),
        ])

        click.echo('Filled.')

        click.echo('Committing...')
        db.session.commit()
        click.echo('Commit succeed.')
