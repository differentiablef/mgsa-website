# ##############################################################################
# This file contains the principle definition of the module.
#   The contents of this file will be hooked into the namespace in which it 
# is imported. In this case to import this module we would add the following 
# to main.py (in the module loading section): 
#    
#    import modules.organization
#

from base import add_content_module
from base import register_data_models
from base.module import ContentModule

org_mod = ContentModule('organization', __name__)

# ##############################################################################
# main menu

org_mod.add_menu('About Us', 'organization.default' )

# ##############################################################################
# side panel menu

org_mod.add_side_menu(
    'Organization/Officers', # Side panel title
    [
        ( 'Update Offices', 'organization.update_offices' ), 
        ( 'Update Officers', 'organization.edit_officer' ),
        ( 'Edit About Us', 'organization.edit_aboutus')
    ],
    'admin'
)

# ##############################################################################
# Load the module implementation

import models # filename: models.py
import views  # filename: views.py

# attach module to website
add_content_module( org_mod )

# register our data models
register_data_models([ models.Office, models.Officer ])




