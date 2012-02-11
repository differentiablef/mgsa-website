# ##############################################################################
# Section: global imports

import mimetypes

# ##############################################################################
# Section: Flask imports

from flask import Flask, flash

# ##############################################################################
# Section: Flask extension imports

from flaskext.sqlalchemy import SQLAlchemy
import flask_sijax as ajax
from flaskext.mail import Mail

# #############################################################################
# Base Initialzation and Config Section

# intialize the application
base_app = Flask('__main__')

# pull in the config file and setup other config variables
base_app.config.from_pyfile('./website.conf')
base_app.config['SQLALCHEMY_DATABASE_URI'] = base_app.config['DATABASE_URI']
base_app.config['SIJAX_JSON_URI'] = '/static/js/json2.js'


# ##############################################################################
# Prepare db enviornment and mailer enviorment

db            = SQLAlchemy( base_app )
mailer        = Mail( base_app )

# #############################################################################
# Section: Local imports

from base.content import Content
from base.database import create_database
from base.utils.gravatar import Gravatar
from base.utils.login import *
from base.utils.lesscss import lesscss

login_manager = LoginManager( )
login_manager.setup_app(base_app)
gravatar = Gravatar(base_app, size=124, 
                    rating='pg', default='retro', 
                    force_default = False, force_lower = False )

base_app.mailer          = mailer
base_app.db              = db
base_app.login_manager   = login_manager
base_app.content_modules = []
base_app.admin_models    = [ Content ]
base_app.gravatar        = gravatar

# initialize Sijax
ajax.Sijax(base_app)

# XXX: This might be a bad idea
#base_app.route = ajax.route

# ##############################################################################
# Setup jinja globals for templates
base_app.jinja_env.globals["content_modules"] = base_app.content_modules
base_app.jinja_env.globals["degrees"] = base_app.config['DEGREE_PROGRAMS']

# #############################################################################
# Section: Test the database, and should the user or role tables fail to exist
#          create them (this must be done :'( )

create_database()

if base_app.debug is True:
    # ##############################################################################
    # Enable less-css compile on demand (see utils/lesscss.py)

    lesscss(base_app)



# ##############################################################################
# Section: Interface functions
# Synop: This section contains interface functions which are used to hook 
#        into and control the websites base

# ##############################################################################
# Name: add_content_module
# Synop: attach the module 'module' to the current application and register all
#        the bits

def add_content_module(module):
    # if base_app.modules.has_key( module._name ):
    #     return
    
    base_app.register_blueprint(module)
    base_app.content_modules.append(module)
    base_app.jinja_env.globals["content_modules"] = base_app.content_modules

# ##############################################################################
# Name: register_data_models
# Synop: register a particular data model with the application 
#
def register_data_models(modelobjList):
    for obj in modelobjList:
        base_app.admin_models.append(obj)

# #############################################################################
# Name: register_user_role
# Synop: add the new role to the table of user roles if it is not already 
#        present

from base.user import Role

def register_user_role(roleName):
	bas = Role.query.filter_by(rolename = roleName).first()
	if bas is None:
		rol = Role()
		rol.rolename = roleName
		db.session.add(rol)
		db.session.commit()


# #############################################################################
# Name: register_content_container
# Synop: add a new content tag place holder with the tag given and default
#        contents given

from base.content import Content

def register_content_container(tag, contents):
    cnt = Content.query.filter_by(tag = tag).first()
    if cnt is None:
        cnt = Content()
        cnt.set_tag(tag)
        cnt.set_contents(contents)
        db.session.add(cnt)
        db.session.commit()

# ##############################################################################
# Name: initialize_admin_interface
# Synop: using our modified version of Flask-Admin, we create and register
#        the admin blueprint to operation with the models that have been 
#        registered using register_data_models

from admin.datastore.sqlalchemy import SQLAlchemyDatastore

def initialize_admin_interface():
    # add the admin interface blueprint
    base_app.admin_datastore = SQLAlchemyDatastore( base_app.admin_models, db.session )
    admin_blueprint = admin.create_admin_blueprint( base_app.admin_datastore, 
                                                    view_decorator = role_required('admin'))
                                                    

    # add the resource/template editor
    # we define this function here for "security reasons"
    @admin_blueprint.route("/resedit/<path:filename>")
    @role_required('admin')
    def _resource_edit(filename):
        print filename
        if '..' in filename or filename.startswith('/'):
            abort(404)

        fil = base_app.open_resource(filename)
        res_contents=fil.read()
        return render_template('admin/code_edit.html', resource_contents = res_contents)

    base_app.register_blueprint(admin_blueprint, url_prefix='/admin')
    

# ##############################################################################
# Section: default_view handler
# 
from flask import render_template

def _default_view( templatename = None, error = None, redirect = None ):

    if error is not None:
        flash(error, 'error');
    
    if templatename is None:
        templatename = 'layout.html'
    if not redirect is None:
    	return redirect(url_for(redirect))
    
    return render_template( templatename, error = error )

base_app.default_view = _default_view

def default_view( *args, **kargs ):
	return base_app.default_view(*args, **kargs)

# ##############################################################################
# name: call_view
# synop: calls the view function for the end-point given with the args given

from flask import url_for, redirect
def call_view(endpoint, *args, **kargs):
    # have to do redirect because of namespace issues
    #    return base_app.view_functions[endpoint](*args,**kargs)
    return redirect(url_for(endpoint, *args, **kargs))


# ##############################################################################
# Section: request and template context setup functions


# ##############################################################################
# Name: inject_functions
# Synop: used to pass functions to the template context

@base_app.context_processor
def inject_functions():
    # ##############################################################################
    # Name: get_content
    # Synop: using the generic Content, query and return the content entries with 
    #        the given name return "" if not found, and 
    #
    def get_content(tagname):
        contnt = Content.query.filter_by(tag = tagname).first()
        if contnt is None:
            return ""
        
        return contnt.get_contents()
    
    return dict( get_content = get_content )


# ##############################################################################
# Name: global_before_request
# Synop: this is the site-wide base_app.before_request which is called on every
#        view

from flask import g, get_flashed_messages
import json

@base_app.before_request
def global_before_request():
    pass

