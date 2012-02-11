
# ##############################################################################
# In here you will find our implementation of various database elements 
# we will use to store information the user provides or whatever. 
# 
# Note: it is recommended that you take a look at the documentation for 
#       Flask-SQLAlchemy (a google search will take you there)

# ##############################################################################
# Import the websites generic database object
#    We use this to hook into the database that the site is connected too, 
# in this we way we only extend what is already there. Moreover, the object 'db'
# provides us with the system we use to define individual models

from base import db

# ##############################################################################
# Name: ExampleTag
# Synop: the class ExampleTag is the generic container for an individual 
#        entry in our database table with the same name (this is the magic
#        of SQLAlchemy.) We define the table and the container all at the same
#        time, and SQLAlchemy does the rest for us.
#
# Note: All models must inherit db.Model. Moreover, the columns of the table 
#       they define will be determined by member variables which are initialized 
#       using the db.Column object/function
#

class ExampleTag(db.Model):
    # Define the main entries which will appear in the table
    # the generic format for this is:
    #
    #   [fieldname] = db.Column( [type], [extra options] )
    #
    
    id       = db.Column( db.Integer, primary_key=True ) # The primary key
    tag_name = db.Column( db.String(100), unique=True )  # A data column: 'name', 
    # which is string of length at most 100
