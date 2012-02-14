
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from flask import g

from base import current_user
from base import login_required
from base import default_view
from base import base_app
from base import ajax

from modules.admin import admin_mod

# ##############################################################################
# Section: view definitions 

@admin_mod.route('/db')
def database_admin():
    return redirect(url_for('admin.index'))

@admin_mod.route('/users')
def user_admin():
    return redirect(url_for('admin.list',model_name='User'))

@admin_mod.route('/mods')
def modules_admin():
    flash("Not Implemented Yet", "Error")
    return base_app.default_view()

@admin_mod.route('/templates')
def templates_admin():
    flash("Not Implemented Yet", "Error")
    return base_app.default_view()

@admin_mod.route('/staticfiles')
def static_admin():
    flash("Not Implemented Yet", "Error")
    return base_app.default_view()
