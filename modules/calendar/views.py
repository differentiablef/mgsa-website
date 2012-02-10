# ##############################################################################
# Package imports
from modules.calendar import calendar_mod as calendar

from models import Event


# ##############################################################################
# Generic imports

from flask import jsonify, Response
from flask import request, session, redirect, url_for, render_template, flash

from time import localtime
from datetime import *

from base.user import User
from base import default_view, login_required, db, current_user, role_required
from base import call_view
# ##############################################################################
# Basic views
@calendar.route('/view')
def default():
    return render_template('calendar.html')

@calendar.route('/viewevent/<int:eventid>', methods=['GET'])
def view_event(eventid):
    event = Event.query.get(eventid);
    
    if event:
        return render_template('show_event.html', event = event)
    
    flash("Invalid Request", "Error")
    return default()


# ##############################################################################
# JSON Export views
@calendar.route('/event.json')
def get_events():
    
    sparm = request.args.get('start', None, type=float)
    eparm = request.args.get('end', None, type=float)
    
    if sparm == None or eparm == None:
        flash("Invalid Request", "Error")
        return default_view()
    
    sdate = datetime.fromtimestamp(sparm)
    edate = datetime.fromtimestamp(eparm)
    
    events = Event.query.filter(Event.date_start >= sdate).\
                        filter(Event.date_end <= edate).all()
    
    json_str = "[ "
    
    for event in events:
        jsobj = {
            'id': event.id,
            'title': event.get_title(),
            'start': event.get_start_date(),
            'end': event.get_end_date(),
            'info': event.get_info(),
            'location': event.get_location(),
            'allDay': event.allday
        }
        
        json_str = json_str + jsonify(jsobj).data + ","
        
    json_str += "{}]"
    
    return Response(json_str, mimetype="application/json")

# ##############################################################################
# Form submit targets

@calendar.route('/update-event', methods=['POST'])
@role_required('calendar')
def update_event():
    eid         = request.form.get('eventid', None, type=int)
    etitle      = request.form.get('eventtitle', None)
    einfo       = request.form.get('eventinfo', None)
    elocation   = request.form.get('eventlocation', None)
    estr_start  = request.form.get('eventstart', None)
    estr_end    = request.form.get('eventend', None)
    estr_allday = request.form.get('eventallday', None)
    
    if eid == None:
        flash("Invalid Request", "Error")
        return default()
    
    evobj = Event.query.get(eid);
    
    if evobj == None:
        flash("Invalid Request", "Error")
        return default_view()
    
    if etitle != None:
        evobj.set_title(etitle)
    
    if einfo != None:
        evobj.set_info(einfo)
    
    if elocation != None:
        evobj.set_location(elocation)
    
    if estr_allday == 'on':
        evobj.set_allday(True)
    else:
        evobj.set_allday(False)
    
    if estr_start != None and estr_end != None:
        estart = datetime.strptime(estr_start, '%m/%d/%Y %I:%M %p')
        eend   = datetime.strptime(estr_end, '%m/%d/%Y %I:%M %p')
        
        evobj.set_start_date(estart)
        evobj.set_end_date(eend)
    else:
        flash("Invalid Request", "Error")
        return default_view()
    
    db.session.commit()
    
    return default()

@calendar.route('/add-event', methods=['POST'])
@role_required('calendar')
def add_event():
    etitle      = request.form.get('eventtitle', None)
    einfo       = request.form.get('eventinfo', None)
    elocation   = request.form.get('eventlocation', None)
    estr_start  = request.form.get('eventstart', None)
    estr_end    = request.form.get('eventend', None)
    estr_allday = request.form.get('eventallday', None)
    
    evobj = Event(current_user.id)
    
    if etitle != None:
        evobj.set_title(etitle)
    else:
        flash("Invalid Request", "Error")
        return default_view()
    
    if einfo != None:
        evobj.set_info(einfo)
    
    if elocation != None:
        evobj.set_location(elocation)
    else:
        flash("Invalid Request", "Error")
        return default_view()
    
    if estr_allday == 'on':
        evobj.set_allday(True)
    else:
        evobj.set_allday(False)
    
    if estr_start != None and estr_end != None:
        estart = datetime.strptime(estr_start, '%m/%d/%Y %I:%M %p')
        eend   = datetime.strptime(estr_end, '%m/%d/%Y %I:%M %p')
        
        evobj.set_start_date(estart)
        evobj.set_end_date(eend)
    else:
        flash("Invalid Request", "Error")
        return default_view()
    
    db.session.add(evobj)
    db.session.commit()

    return default()

# ##############################################################################
# Section: Admin Views

@calendar.route('/admin-add-event')
@role_required('admin')
def admin_add_event():
     return call_view('admin.add', model_name='Event')

@calendar.route('/admin-list-events')
@role_required('admin')
def admin_list_events():
    return call_view('admin.list', model_name='Event')
    
