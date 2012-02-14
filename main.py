
# ##############################################################################
# Local imports and initialization

from base import base_app, initialize_admin_interface
from base.user_auth import *

# ##############################################################################
# Load website content modules

import modules.news
import modules.articles
import modules.seminars
#import modules.example
import modules.calendar
import modules.organization
import modules.usertools
import modules.admin

# ##############################################################################
# Load development code

import development

# ##############################################################################
# Principal routes

from flask import render_template, url_for, redirect, flash, g
from base import call_view, ajax

@base_app.login_manager.unauthorized_handler
def unauthorized_user():
    return render_template('unauthorized_user.html') 

@base_app.route('/', methods=['POST', 'GET'])
def default( templatename = None, error = None, redirect_func = None ):
    if not error is None:
        flash(error, 'error');
        
        if not redirect_func is None:
            return call_view(redirect_func)
        
        if templatename is None:
            return redirect(url_for('news.default'))
    
    if templatename is None:
        templatename = 'layout.html'
    
    return render_template( templatename )

base_app.default_view = default

# ##############################################################################
# Name: sijax_base_res

@ajax.route(base_app, "/ajax")
def sijax_base_res():
    if g.sijax.is_sijax_request:
        return g.sijax.process_request()

# ##############################################################################
# Finalize and execute

initialize_admin_interface()

# ##############################################################################
# Debug stuff
from base.debug import DebugToolbarExtension
toolbar = DebugToolbarExtension(base_app)


if __name__ == '__main__':
    base_app.run()

