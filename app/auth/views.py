from datetime import datetime
from flask import request,render_template, session, redirect, url_for

from . import auth
from .forms import LoginForm
from .helper import apiv1_prefix

@auth.route(apiv1_prefix('/manager/getToken'),method=['POST'])
def get_token():
    pass
