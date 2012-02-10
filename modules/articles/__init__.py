
# ######################################################################3#######
# imports
from base import base_app, add_content_module, register_data_models, url_for 
from base import register_user_role
from base.module import ContentModule


# ######################################################################3#######
# Initialization
articles_mod = ContentModule('articles', __name__)

articles_mod.add_menu('Articles', 'articles.default' )
articles_mod.add_side_menu(
    'Articles', 
    [
        ('Add Article', 'articles.add_article'),
        ('Edit Articles', 'articles.update_articles')
    ],
    'admin'
)

import models
import views

# ######################################################################3#######
# Hooking into main website

add_content_module( articles_mod )

# ######################################################################3#######
# Register data models

register_data_models( [ models.Article, models.Article_Comment ] )

# ##############################################################################
# register user roles
register_user_role('contributor')
