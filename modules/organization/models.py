
from base import db
from base.user import User

# ##############################################################################
# Name: Office/Officer
# Basic containers for offices and officer positions
class Office(db.Model):
    id          = db.Column( db.Integer, primary_key=True ) # The primary key
    name        = db.Column( db.String(200), unique=True )
    description = db.Column( db.Text )
    officer_id  = db.Column(db.Integer, db.ForeignKey("officer.id"))
    def __repr__(self):
        return "%s" % (self.name)


class Officer(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	holder_id = db.Column(db.Integer, db.ForeignKey("user.id"))
	holder = db.relationship("User")
	offices = db.relationship("Office", backref = "Officer")
	
	def __repr__(self):
		return "%s" % (self.holder.get_fullname())
	
	def get_offices(self):
		chunk = ""
		for off in self.offices:
			if not chunk == "":
				chunk += ", "
				 
			chunk += str(off.name)
		
		return chunk
	
	def get_duties(self):
		chunk = ""
		for off in self.offices:
			chunk += "<h4>As " + off.name + "</h4><p>" + str(off.description) + "</p>"
		return chunk

 