
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
    pass

@ajax.route(admin_mod, '/users')
def user_admin():

    flash("interesting", "message")    
    
    if g.sijax.is_sijax_request:
        return g.sijax.process_request()
        
    frm = base_app.admin_datastore.get_model_form('User')
    return render_template('base_form.html',form=frm())

@admin_mod.route('/mods')
def modules_admin():
    pass

@admin_mod.route('/templates')
def templates_admin():
    pass

@admin_mod.route('/staticfiles')
def static_admin():
    pass
