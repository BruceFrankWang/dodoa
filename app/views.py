# -*- coding: utf-8 -*-

"""
    DODOA
        A better OA system for Design Management.
    
    :Author:    Bruce Frank Wang
    :File Time: 2019-02-20 13:01
    :copyright: © 2019 Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :license:   GPL v3, see LICENSE for more details.
"""

from flask import Blueprint, render_template

from app.models import Project


bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/project')
def project_brief():
    project_list = Project.query.all()
    return render_template('project_brief.html', project_list=project_list)


@bp.route('/project/<name>')
def project(name):
    p = Project.query.filter_by(name=name).first_or_404()
    return render_template('project.html', project=p)


@bp.route('/plan')
def plan():
    return render_template('plan.html')


@bp.route('/resource')
def resource():
    return render_template('resource.html')


@bp.route('/employee')
def employee():
    return render_template('employee.html')
