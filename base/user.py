
# ##############################################################################
# Here you will find the site wide user object and interfaces

from base import db

table_user_roles = db.Table('user_roles',
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

# #############################################################################
# Name: Role
# Synop: Abstract group container, used to specify user privileges 
#        considered as roles.
# 

class Role(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    rolename  = db.Column(db.String(120), unique=True)
    
    def __repr__(self):
        return self.rolename

# #############################################################################
# Name: User 
# Synop: Basic user model for login, and tagging
#

class User(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    username       = db.Column(db.String(120), unique=True)
    password       = db.Column(db.String(300))
    email          = db.Column(db.String(120), unique=True)
    active         = db.Column(db.Boolean)
    nickname       = db.Column(db.String(120))
    firstname      = db.Column(db.String(120))
    lastname       = db.Column(db.String(120))
    uncc_email     = db.Column(db.String(120))
    degree_program = db.Column(db.Integer)
    roles          = db.relationship('Role', secondary='user_roles', 
                                     backref=db.backref('users', lazy='dynamic'))
    
    # #############################################################################
    # Basic constructor definitions
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.email = email
        self.password = password
        self.active = True
    
    def __repr__(self):
        return '%s %s' % (self.firstname, self.lastname)


    # ##########################################################################
    # Implement basic interface functions

    def set_fullname(self,first, last):
        self.firstname = first
        self.lastname = last

	def set_email(self, email):
		self.email = email
	
    def set_uncc_email(self,email):
        self.uncc_email = email

    def set_degree_program(self,program):
        self.degree_program = program

    def set_nickname(self,nick):
        self.nickname = nick

    def set_active(self,state):
        self.active = state

    def add_role(self, rol):
        rl = Role.query.filter_by( rolename = rol ).first()
        if not rl is None:
            self.roles.append( rl )
    
    def get_fullname(self):
    	return "%s %s" % (self.firstname, self.lastname)
    	
    def get_display_name(self):
        return self.nickname

    # #############################################################################
    # Implementation of LoginManager required functions
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return self.active
        
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)


    # #########################################################################
    # Additional Permissions via Roles  
    def has_role(self, role_name):
        for role in self.roles:
            if role_name == role.rolename:
                return True
            elif role.rolename == 'admin':
                return True
        return False

