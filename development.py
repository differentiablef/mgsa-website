
from base import base_app, default_view
from flask import g, render_template
from flaskext.mail import Message


@base_app.route('/extern/<path>')

@base_app.route('/dev')
def forum_wrap():
    return render_template("layout.iframewrap.html", target="/extern/forum/index.php")


def mailer():

    msg = Message("client test")
    msg.add_recipient("mblack44@uncc.edu")

    msg.body = "Yo, shoot me a message"

    base_app.mailer.send(msg)
    
    return default_view()

