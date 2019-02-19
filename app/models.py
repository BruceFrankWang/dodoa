# -*- coding: utf-8 -*-

"""
    DODOA
        A better OA system for Design Management.
    
    :Author:    Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :Time:      2019-02-20 02:15
    :copyright: © 2019 Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :license:   MIT, see LICENSE for more details.
"""

from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    code = db.Column(db.String)
