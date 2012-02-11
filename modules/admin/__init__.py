# ##############################################################################
# Basic Admin Interface
#    -> Allows editing of individual models registered by other modules
#    -> Create static/template pages
#    -> Update templates/js/css files
#
#    import modules.admin
#

from base import add_content_module
from base import register_data_models
from base import register_user_role
from base import url_for
from base.module import ContentModule

# ##############################################################################
# Define the ContentModule object 

admin_mod = ContentModule('admin', __name__)

# ##############################################################################
# Add admin side panel menu

admin_mod.add_side_menu(
    'Administration', # Side panel title
    [
        # A link which will be in the side-menu
        # the format is: ([Name], [target])
        ( 'Database', 'ifadmin.database_admin' ), 
        ( 'Users', 'ifadmin.user_admin' ), 
        ( 'Modules', 'ifadmin.modules_admin' ),
        ( 'Templates', 'ifadmin.templates_admin' ),
        ( 'Static Files', 'ifadmin.static_admin' )
    ],
    'admin'
)

# ##############################################################################
# Load views
import views  # filename: views.py

# ##############################################################################
# Finally we hook the module into the main website

add_content_module( admin_mod )
