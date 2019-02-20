# -*- coding: utf-8 -*-

"""
    DODOA
        A better OA system for Design Management.
    
    :Author:    Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :Time:      2019-02-20 01:20
    :copyright: © 2019 Bruce Frank Wang <bruce.frank.wang@gmail.com>
    :license:   GPL v3, see LICENSE for more details.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
