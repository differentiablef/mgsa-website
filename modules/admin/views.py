
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect

from base import current_user
from base import login_required
from base import default_view
from base import base_app

from modules.admin import admin_mod

# ##############################################################################
# Section: view definitions 

@admin_mod.route('/db')
def database_admin():
    pass

@admin_mod.route('/users')
def user_admin():
    pass

@admin_mod.route('/mods')
def modules_admin():
    pass

@admin_mod.route('/templates')
def templates_admin():
    pass

@admin_mod.route('/staticfiles')
def static_admin():
    pass
