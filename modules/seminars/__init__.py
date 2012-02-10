
from base import add_content_module
from base import register_data_models
from base import register_user_role
from base import url_for
from base.module import ContentModule

# ##############################################################################
# Define the ContentModule object which will hook into the main website
# the first argument specifies the modules 'name', and the second specifies the 
# package that contains the module.
#

seminar_mod = ContentModule('seminars', __name__)

# ##############################################################################
# Add a main menu entry

seminar_mod.add_menu('Seminars', 'seminars.default')

# ##############################################################################
# Add a side panel menu

seminar_mod.add_side_menu(
    'Seminars', # Side panel title
    [
        ( 'Add Seminar', 'seminars.add_seminar' ), 
        ( 'Edit Seminars', 'seminars.update_seminars' ),
        ( 'Edit Talks', 'seminars.update_talks' )
    ],
    'seminar-organizer'
)

# ##############################################################################
# Load the module implementation

import models # filename: models.py
import views  # filename: views.py

# attach module to website
add_content_module( seminar_mod )

# register our data models
register_data_models([ models.Seminar, models.Talk ])

# register user roles
register_user_role('seminar-organizer')
