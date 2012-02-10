
# ##############################################################################
# Module: usertools
# Synop: A collection of views which allow the user to update his/her profile
#        and provides a sidepane menu including links for logout, and others
#        actions
# Menus:
#     Main menu: none
#     Side menu: user info access, and logout
#

from base import add_content_module, register_data_models, url_for
from base.module import ContentModule
from base.user import Role, User

usertools_mod = ContentModule('usertools', __name__)

usertools_mod.add_side_menu(
    'User', # Side panel title
    [
        ( 'Update Information', 'user_update' ),
        ( 'Logout', 'auth_logout' )
    ]
)

# attach module to website
add_content_module( usertools_mod )

register_data_models([User, Role])