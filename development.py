
from base import base_app, default_view
from flask import g, render_template
from flaskext.mail import Message
from base import ajax

@base_app.route('/extern/<path>')

@ajax.route(base_app,'/dev', methods=['POST', 'GET'])
def forum_wrap():
    if g.sijax.is_sijax_request:
        return g.sijax.process_request()
    
    return default_view()


def mailer():

    msg = Message("client test")
    msg.add_recipient("mblack44@uncc.edu")

    msg.body = "Yo, shoot me a message"

    base_app.mailer.send(msg)
    
    return default_view()

