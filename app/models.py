# -*- coding: utf-8 -*-

"""
    DODOA
        A better OA system for Design Management.
    
    :Author:    Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :Time:      2019-02-20 02:15
    :copyright: © 2019 Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :license:   GPL v3, see LICENSE for more details.
"""

from app import db


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    name_zh = db.Column(db.String, nullable=False, unique=True)
    employee_list = db.relationship('Employee',
                                    backref=db.backref('gender', lazy='joined'),
                                    lazy='dynamic'
                                    )

    def __repr__(self):
        return "<Gender (name='{name}')>".format(name=self.name)


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    employee_list = db.relationship('Employee',
                                    backref=db.backref('specialty', lazy='joined'),
                                    lazy='dynamic'
                                    )

    def __repr__(self):
        return "<Specialty (name='{name}')>".format(name=self.name)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date)
    accession_day = db.Column(db.Date)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialty.id'), nullable=False)

    def __repr__(self):
        return "<Employee (name='{name}')>".format(name=self.name)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    code = db.Column(db.String)
    location = db.Column(db.String)

    def __repr__(self):
        return "<Project (name='{name}')>".format(name=self.name)


class LandBlock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)

    def __repr__(self):
        return "<LandBlock (name='{name}')>".format(name=self.name)


class DesignStandard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<DesignStandard (name='{name}')>".format(name=self.name)
