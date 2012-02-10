

from base import add_content_module
from base import register_data_models
from base import register_user_role
from base import url_for
from base.module import ContentModule

calendar_mod = ContentModule('calendar', __name__)

calendar_mod.add_menu('Calendar', 'calendar.default' )
calendar_mod.add_side_menu(
    'Calendar',
    [
        ('Daily View', 'calendar.default'),
        ('Weekly View', 'calendar.default'),
        ('Monthly View', 'calendar.default')
    ]
)

calendar_mod.add_side_menu(
    'Calendar Events',
    [
        ('Add Event', 'calendar.admin_add_event'),
        ('List Events', 'calendar.admin_list_events')
    ],
    'admin'
)


import models
import views

add_content_module(calendar_mod)

# register the data models with base
register_data_models( [ models.Event ] )

# register required roles to base for enforcment
register_user_role('calendar')
