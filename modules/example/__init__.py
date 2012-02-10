# ##############################################################################
# This file contains the principle definition of the module.
#   The contents of this file will be hooked into the namespace in which it 
# is imported. In this case to import this module we would add the following 
# to main.py (in the module loading section): 
#    
#    import modules.example
#

from base import add_content_module
from base import register_data_models
from base import url_for
from base.module import ContentModule

# ##############################################################################
# Define the ContentModule object which will hook into the main website
# the first argument specifies the modules 'name', and the second specifies the 
# package that contains the module.
#

example_mod = ContentModule('example', __name__)

# ##############################################################################
# Add a main menu entry
#      The display name in this case will be: Example
#        And the target for the link will be: url_for('example.default')
#
# Note: when we specify a link for a view in a module, we do so with the 
#       convention: [module name].[function name]
# 
# Note: we can add more than one menu entry by calling this function again
#

example_mod.add_menu('Example', 'example.default')

# ##############################################################################
# Add a side panel menu
#    At this point it seems like a decent idea to give a user which has loggedin 
# a list of newly accessible functions they can use.
#   We accomplish this by using the add_side_menu function from ContentModule
# where the first argument is the title of the side panel section, and the 
# second is a list of links which will be injected into the panel

example_mod.add_side_menu(
    'Example Menu One', # Side panel title
    [
        # A link which will be in the side-menu
        # the format is: ([Name], [target])
        ( 'Item 1', 'example.callback' ), 
        ( 'Item 2', 'example.callback' ), 
        ( 'Item 3', 'example.another_callback' ),
        ( 'Item 4', 'example.another_callback' )
    ]
)

# ##############################################################################
# Load the module implementation
#    Here we have split the module into two parts models and views. The 
# views will govern how the user interacts with the content, and will determine
# how we extend the main template: layout.html. In addition, the models consist of 
# database objects which this module implements and uses.
#

import models # filename: models.py
import views  # filename: views.py

# ##############################################################################
# Finally we hook the module into the main website
#    we do this by calling the function add_content_module( [module obj] ) 
# after we have imported all the relavent implementations. And we call 
# the function register_data_model( [datamodel type] ) to inform the admin
# system about the models we have defined in this module

# attach module to website
add_content_module( example_mod )

# register our data models
register_data_models([ models.ExampleTag ])
