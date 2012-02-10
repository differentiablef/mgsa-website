
from base import base_app, db
from base.user import table_user_roles, Role, User


def create_database():
    class __generated_db(db.Model):
        id = db.Column(db.Integer, primary_key=True)
	
    try:
        __generated_db.query.all()
    except: # Only way we get here is if the table does not exist
        # Initialize the database, and should it fail to exist, create an empty one 
        db.create_all()
        
        cookie = __generated_db()
        db.session.add(cookie)
        db.session.commit()

