# ##############################################################################
# Here you will find the implemenation of the views which comprise this 
# module

# ##############################################################################
# Section: Generic imports
#   (here we import functions we will use to render the views)
# Note: It is recommended that you become familiar with the use of the Flask
#       web framework (a google search for 'python Flask' will yeild what you
#       want)

from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect

from base import current_user
from base import login_required
from base import default_view
from base import base_app

# ##############################################################################
# Section: import the ContentModule object we created in __init__.py
#
# NOTE: the names below correspond to directories which are packages
#       and the following line should be seen as a path for it to
#       make sense: translating it is 'modules/example/' 
#       since our intention is to import this package, all names are 
#       taken relative to the root directory containing main.py
#

from modules.example import example_mod

# ##############################################################################
# Section: Now, we are going to implement the views for this module and 
#          following the Flask setup they come in the following form
#
#               @[module obj].route( [relative url path], [...])
#               [function definition]
#

# ##############################################################################
# Name: default
# Synop: this will serve as the entry point for our module (not in the normal
#        sense) it is just the function we use to handle the main menu link
#        which is accessible to everybody

@example_mod.route('/view')
def default():
    text = "default function"
    
    return render_template('blank.html', example_text = text)


# ##############################################################################
# Names: callback, another_callback
# Synop: here we implement one of the two views that will be opened to the 
#        user after they login. To ensure that the user is logged in, we have 
#        a pair of options
@example_mod.route('/item')
def callback():
    text = "callback function"
    return render_template('blank.html', example_text = text)

@example_mod.route('/another_item')
def another_callback():
    text = "another_callback function"
    return render_template('blank.html', example_text = text)



