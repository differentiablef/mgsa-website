# ##############################################################################
# Section: Generic imports

from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect
from flask import g

from base.content import Content
from base import request
from base import current_user
from base import login_required
from base import role_required
from base import default_view
from base import base_app
from base import call_view

# ##############################################################################
# local imports

from modules.organization import org_mod
from models import Office, Officer


# ##############################################################################
# Name: default
# Synop: this will serve as the entry point for our module (not in the normal
#        sense) it is just the function we use to handle the main menu link
#        which is accessible to everybody

@org_mod.route('/view')
def default():
    offi = Officer.query.all()
    org_info = Content.query.filter_by(tag = 'about-us').first()
    return render_template('about-us.html',  officers = offi, 
                           organization_info = org_info.get_contents())


# ##############################################################################
# Section: Interface View definitions 

@org_mod.route('/update-officers')
@role_required('admin')
def update_offices():
    
    return call_view('admin.list', model_name='Office')

@org_mod.route('/edit-officer')
@role_required('admin')
def edit_officer():
    return call_view('admin.list', model_name='Officer')

@org_mod.route('/edit-aboutus', methods=['POST','GET'])
@role_required('admin')
def edit_aboutus():
    cnt = Content.query.filter_by(tag= 'about-us').first()
    return call_view('admin.edit', model_name = 'Content', model_url_key = cnt.id.__repr__())


