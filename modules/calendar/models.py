
# #############################################################################
# Name: Event 
# Synop: Basic event model for calender
#
from time import localtime
from datetime import *

from base.user import User
from base import db

class Event(db.Model):
    id        = db.Column(db.Integer, primary_key=True) 
    title     = db.Column(db.String(80))  # event title
    information     = db.Column(db.Text)  # information about event
    date_start   = db.Column(db.DateTime)    # date event will be
    date_end     = db.Column(db.DateTime)   #
    date_pub  = db.Column(db.DateTime)    # date listed 
    author    = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)     # id of author
    location  = db.Column(db.String(200)) # Location of the event
    allday    = db.Column(db.Boolean)
    
    user = db.relationship("User", backref='events')
    
    
    def __init__(self, author=1):
        
        self.title = ""
        self.information = ""
        self.location = ""
        self.author  = author
        self.date_start = datetime.utcnow()
        self.date_end   = datetime.utcnow() + timedelta(hours=1)
        self.allday     = False
        self.date_pub   = datetime.utcnow()
    
    def __repr__(self):
        return '%s at %s' % (self.title, self.date_start.ctime())
        
    
    # #############################################################################
    # Interface functions
    def get_display_name(self):
        return User.query.get(self.author).get_display_name();

    def set_title(self, title):
        self.title = title
    
    def set_info(self, event_info):
        self.information = event_info
        
    def set_start_date(self, event_date):
        self.date_start = event_date
        
    def set_end_date(self, event_date):
        self.date_end = event_date
    
    def set_location(self, location):
        self.location = location
    
    def set_allday(self, allday):
        self.allday = allday
    
    def get_title(self):
        return self.title
    
    def get_info(self):
        return self.information
    
    def get_start_date(self):
        return self.date_start.ctime()
    
    def get_end_date(self):
        return self.date_end.ctime()
    
    def get_date(self):
        return self.date_start.strftime('%m/%d/20%y')
        
    def get_start_time(self):
        return self.date_start.strftime('%I:%M')
    
    def get_durration(self):
        return self.date_end - self.date_start

    def get_location(self):
        return self.location;

