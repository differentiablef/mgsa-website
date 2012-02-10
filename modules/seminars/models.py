
# ##############################################################################
from base import db

# #############################################################################
# Name: Seminar
# Synop: Basic model for a seminar object

class Seminar(db.Model):
    id    = db.Column( db.Integer, primary_key=True ) # The primary key
    title  = db.Column( db.String(300), nullable=False )  # A data column: 'name',
    
    Organizer_id = db.Column( db.Integer, db.ForeignKey('user.id'))
    Organizer = db.relationship( "User", backref="seminars")
    
    private = db.Column(db.Boolean)
    description = db.Column( db.Text, nullable = False )
    talks = db.relationship( "Talk" )
    website = db.Column(db.String(500))

    contact_name = db.Column(db.String(500))
    contact_email = db.Column(db.String(500))

    def get_location(self):
        return self.location

    def get_contact_name(self):
        return self.contact_name
    
    def get_contact_email(self):
        return self.contact_email
    
    def get_title(self):
        return self.title

    def get_website(self):
        return self.website

    def get_organizer_name(self):
        return self.Organizer.get_display_name()

    def get_description(self):
        return self.description

    def is_private(self):
        return self.private

    def __repr__(self):
        return self.title

    
    


# #############################################################################
# Name: Talk
class Talk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(350), nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    date_of = db.Column(db.DateTime, nullable=False)
    
    seminar_id = db.Column(db.Integer, db.ForeignKey("seminar.id"))
    seminar = db.relationship("Seminar")

    speaker = db.Column(db.String(500), nullable=False)
    speaker_info = db.Column(db.Text)

    
    location = db.Column(db.String(500))

    def get_location(self):
        return self.location

    def get_date(self):
        return self.date_of.strftime('%m/%d/20%y %I:%M %p');

    def get_abstract(self):
        return self.abstract

    def get_speaker(self):
        return self.speaker

    def get_speaker_info(self):
        return self.speaker_info

    def get_topic(self):
        return self.topic

    def __repr__(self):
        return ("%s (%s) on %s" % (self.topic, self.seminar.title, self.get_date()))