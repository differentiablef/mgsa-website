
# ######################################################################3#######
# imports
from base import base_app, add_content_module, register_data_models, url_for
from base.module import ContentModule


# ######################################################################3#######
# Initialization
newsMod = ContentModule('news', __name__)

newsMod.add_menu('News', 'news.default' )
newsMod.add_side_menu(
    'News', 
    [
        ('Add Post', 'news.add_post'),
        ('List Posts', 'news.admin_list_posts')
    ],
    'admin'
)

import models
import views

# ######################################################################3#######
# Hooking into main website

add_content_module( newsMod )

# ######################################################################3#######
# Register data models

register_data_models( [ models.NewsPost, models.NewsPostComment ] )

