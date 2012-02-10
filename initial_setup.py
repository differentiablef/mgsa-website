#!env/bin/python

# ####################################################################
# This is the initial configuration script
#    The tasks of this script are as follows:
#  1) Setup the database with the initial objects
#  2) configure each module
#  3) preform any other first-run initializations

from main import base_app

# #############################################################################
# Section: Database setup

base_app.db.create_all()

# #############################################################################
# Section: Basic user and role setup

from base.user import User
from base.user import Role

rls = base_app.config['DEFAULT_ROLES']
for rol in rls:
    rl = Role()
    rl.rolename = rol
    base_app.db.session.add(rl)

base_app.db.session.commit()

admin_uname = base_app.config['DEFAULT_ADMIN_USER'][0]
admin_pwhash = base_app.config['DEFAULT_ADMIN_USER'][1]
admin_email = base_app.config['DEFAULT_ADMIN_USER'][2]
admin_umail = base_app.config['DEFAULT_ADMIN_USER'][3]

admin_fname = base_app.config['DEFAULT_ADMIN_USER'][4]
admin_lname = base_app.config['DEFAULT_ADMIN_USER'][5]
admin_nickname = base_app.config['DEFAULT_ADMIN_USER'][6]

usr = User( admin_uname, admin_pwhash, admin_email )

usr.set_fullname( admin_fname, admin_lname )
usr.set_nickname( admin_nickname )
usr.set_uncc_email( admin_umail )

usr.add_role('admin')

base_app.db.session.add(usr)

# #############################################################################
# Section: module specific configuration and initial population

from base import register_content_container

# #############################################################################
# Module: organization
# Synop: Populate the UserOffice table with the contents provided in config

from modules.organization.models import Office

offices = base_app.config['ORGANIZATION_OFFICES']

for oid, (title, desc) in offices.iteritems():
	offi = Office()
	offi.id = oid
	offi.name = title
	offi.description = desc
	base_app.db.session.add(offi)


# register about-us content-container
register_content_container( 'about-us', base_app.config['ORGANIZATION_INFO'])

# #############################################################################
# Section: Final Commit
base_app.db.session.commit()



