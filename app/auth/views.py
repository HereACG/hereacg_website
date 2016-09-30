from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import auth
from .forms import LoginForm
from .helper import apiv1_prefix

@auth.route(apiv1_prefix('/register/<username>'))
def register():
    pass
