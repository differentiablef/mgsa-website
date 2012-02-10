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
from flask import redirect, request
from base import role_required
from base import current_user
from base import login_required
from base import default_view
from base import base_app

from datetime import *

# ##############################################################################
# Section: import the ContentModule object we created in __init__.py

from modules.seminars import seminar_mod
from models import Seminar, Talk

# ##############################################################################
# Section: views

# ##############################################################################
# Name: default
# Synop: this will serve as the entry point for our module 

@seminar_mod.route('/view')
def default():
    seminars = Seminar.query.all()
    return render_template('view_seminars.html', seminars = seminars)


# ##############################################################################
# Names: add_seminar, update_seminars

@seminar_mod.route('/add', methods=[ 'GET', 'POST' ])
@role_required('seminar-organizer')
def add_seminar():
    
    if request.method == 'POST':
        # This assumes client-side validation
        sem = Seminar()
        sem.Organizer_id = current_user.id 
        sem.title = request.form.get("title")
        if request.form.get("private") == 'on':
            sem.private = True
        else:
            sem.private = False

        sem.description =request.form.get("description") 
        sem.website = request.form.get("website")
        sem.contact_name = request.form.get("contact_name")
        sem.contact_email = request.form.get("contact_email")
        base_app.db.session.add(sem)
        base_app.db.session.commit()
        flash("Added seminar: %s" % sem.title, "Success")
        return default()
    
    return render_template('add_seminar.html')

@seminar_mod.route('/edit')
@role_required('seminar-organizer')
def update_seminars():
    seminars = Seminar.query.all()
    return render_template('update_seminars.html', seminars = seminars)

# ##############################################################################
# Names: edit_seminar, view_seminar, delete_seminar

@seminar_mod.route("/view/<int:seminarid>")
def view_seminar(seminarid):
    sem = Seminar.query.get(seminarid)
    if sem is None:
        flash("Seminar Not Found", "Error")
        return default()
    
    return render_template('view_seminar.html', seminar=sem)

@seminar_mod.route("/edit/<int:seminarid>", methods=['POST', 'GET'])
@role_required('seminar-organizer')
def edit_seminar(seminarid):
    sem = Seminar.query.get(seminarid)
    
    if sem is None:
        flash("No Such Seminar", "Error")
        return default()

    if request.method == 'POST':
        if sem.Organizer_id == current_user.id or current_user.has_role('admin'): 
            sem.title = request.form.get("title")
            
            if request.form.get("private") == 'on':
                sem.private = True
            else:
                sem.private = False
    
            sem.description =request.form.get("description") 
            sem.website = request.form.get("website")
            sem.contact_name = request.form.get("contact_name")
            sem.contact_email = request.form.get("contact_email")

            base_app.db.session.commit()
            flash("Updated seminar: %s" % sem.title, "Success")
            return default()
        else:
            flash("Insufficient Permissions", "Error")
            return default()
    
    return render_template('edit_seminar.html', seminar = sem)

@seminar_mod.route("/delete/<int:seminarid>")
@role_required('seminar-organizer')
def delete_seminar(seminarid):
    sem = Seminar.query.get(seminarid)

    if sem is None:
        flash("No Such Seminar", "Error")
        return default()

    if sem.Organizer.id == current_user.id or current_user.has_role('admin'):
        for talk in sem.talks:
            base_app.db.session.delete(talk)
        base_app.db.session.delete(sem)
        base_app.db.session.commit()
        
        flash("Seminar Deleted", "Success")
    
    return default()

# ##############################################################################
# Names: add_talk_seminar, edit_talk_seminar, delete_talk_seminar

@seminar_mod.route('/updatetalk')
@role_required('seminar-organizer')
def update_talks():
    sems = Seminar.query.all()
    return render_template('update_talks.html', seminars=sems)

@seminar_mod.route("/addtalk/<int:seminarid>", methods=['POST', 'GET'])
@role_required('seminar-organizer')
def add_talk_seminar(seminarid):
    sem = Seminar.query.get(seminarid)

    if sem is None:
        flash("No Such Seminar", "Error")
        return default()

    if request.method == 'POST': 
        if sem.Organizer_id == current_user.id or current_user.has_role('admin'): 
            talk = Talk()
            talk.topic = request.form.get("topic")
            talk.abstract = request.form.get("abstract")
            talk.date_of = datetime.strptime(request.form.get("date_of"), '%m/%d/%Y %I:%M %p')
            talk.seminar_id = seminarid
            talk.speaker = request.form.get("speaker")
            talk.speaker_info = request.form.get("speaker_info") 
            talk.location = request.form.get("location")
            base_app.db.session.add(talk)
            base_app.db.session.commit()
            flash("Talk added for seminar %s" % sem.title, "Success")
            return default()
        else:
            flash("Insufficient Permissions", "Error")
            return default()

    return render_template('add_talk.html', seminar=sem)

@seminar_mod.route("/edittalk/<int:talkid>", methods=['POST','GET'])
@role_required('seminar-organizer')
def edit_talk_seminar(talkid):
    tlk = Talk.query.get(talkid)

    if tlk is None:
        flash("No Such Talk", "Error")
        return default()

    if request.method == 'POST': 
        if tlk.seminar.Organizer_id == current_user.id or current_user.has_role('admin'): 
            talk = tlk
            talk.topic = request.form.get("topic")
            talk.abstract = request.form.get("abstract")
            talk.date_of = datetime.strptime(request.form.get("date_of"), '%m/%d/%Y %I:%M %p')
            talk.speaker = request.form.get("speaker")
            talk.speaker_info = request.form.get("speaker_info") 
            talk.location = request.form.get("location")
            
            base_app.db.session.commit()

            flash("Talk updated for seminar %s" % talk.seminar.title, "Success")
            return default()
        else:
            flash("Insufficient Permissions", "Error")
            return default()
    
    return render_template("edit_talk.html", talk=tlk)

@seminar_mod.route("/deletetalk/<int:talkid>")
@role_required('seminar-organizer')
def delete_talk_seminar(talkid):
    tlk = Talk.query.get(talkid)
    if tlk is None:
        flash("No Such Talk", "Error")
        return default()

    if current_user.id == tlk.seminar.Organizer_id or current_user.has_role('admin'):
        base_app.db.session.delete(tlk)
        base_app.db.session.commit()
        flash("Talk successfully removed", "Success")

    return default()

