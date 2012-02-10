
from base import login_manager, base_app, default_view, db, flash
from base.user import User
from utils.login import *

from flask import render_template
from bcrypt import hashpw, gensalt

# ##############################################################################
# Implements basic user loader for LoginManager

@login_manager.user_loader
def _load_user(userid):
    return User.query.get(int(userid))


# ##############################################################################
# Implement base login, logout, and register routes

@base_app.route('/logout')
def auth_logout():
    logout_user()
    return default_view()

@base_app.route('/login', methods=['POST'])
def auth_login():
    if request.method == 'POST':
        
        uname = str(request.form['username'])
        pw    = str(request.form['password'])
        quser = User.query.filter_by(username = uname).first()
        
        if( quser != None ):
            
            pw_hash = hashpw(pw, quser.password)

            if( pw_hash == quser.password ):
                login_user(quser)
            else:
                flash('Invalid Username or password', 'Error')
        else:
            flash('Invalid Username or password', 'Error')
    
    return default_view()

@base_app.route('/register', methods=[ 'GET', 'POST' ])
def auth_register():
    error = None
    # #############################################################
    # TODO: Add form input validation and sanitize everything and 
    #        add bcrypt support
    if request.method == 'POST':
        uname       = str(request.form['username'])
        pw          = str(request.form['password'])
        pw2         = str(request.form['password2'])
        email       = str(request.form['email'])
        unc_email   = str(request.form['uncc_email'])
        fname       = str(request.form['firstname'])
        lname       = str(request.form['lastname'])
        nick        = str(request.form['nickname'])
        degree_prog = int(request.form['degree_program'])

        if len(uname) < 5:
            flash('Username is too short: must be longer than five characters', 'Error')
            return render_template('register.html', 
                    error=error,
                    degrees=app.config['DEGREE_PROGRAMS'])

        quser = User.query.filter_by(username = uname).first()
        qemail = User.query.filter_by(uncc_email = unc_email).first()
        
        if (quser is None) and (qemail is None):
            if pw == pw2: # basic password validation
                # generate password hash 
                passwd = hashpw(pw, gensalt())
                
                usr = User(uname, passwd, email)
                usr.set_fullname(fname,lname)
                usr.set_uncc_email(unc_email)
                usr.set_nickname(nick)
                usr.set_degree_program(degree_prog)

                db.session.add(usr)
                db.session.commit()

                flash('User created: You may now login.', 'Message')

                return default_view()
            else:
                flash('Passwords do not math', 'Error')
        else:
            flash('Username or Email already in use.', 'Error')
    return default_view('user/register.html')


# ##############################################################################
# Name: user_update
# Synop: provides a form allowing the user to update their information
@base_app.route('/user-update')
@login_required
def user_update():
    return render_template('user/update_user.html', user = current_user)

# ##############################################################################
# Name: user_update_submit
# Synop: provides a form allowing the user to update their information
@base_app.route('/user-update', methods=['POST'])
@login_required
def user_update_submit():
	error = None
	usr = current_user
	
	fname = request.form.get('firstname', None)
	lname = request.form.get('lastname', None)
	nname = request.form.get('nickname', None)
	dprog = request.form.get('degree_program', None)
	uemai = request.form.get('uncc_email', None)
	email = request.form.get('email', None)
	cpass = request.form.get('curpassword', None)
	pass1 = request.form.get('newpassword', None)
	pass2 = request.form.get('newpassword2', None)
	
	if not fname is None:
		usr.set_fullname(str(fname), str(lname))
		usr.set_nickname(str(nname))
		usr.set_degree_program(int(dprog))
	
	if not uemai is None:
		usr.set_uncc_email(uemai)
		usr.set_email(email)
	
	if not cpass is None:
		pw_hash = hashpw(cpass, usr.password)
		if pw_hash == usr.password:
			if pass1 == pass2:
				usr.password = hashpw(pass1, usr.password)
			else:
				flash("Passwords Fail to Match", "Error")
		else:
			flash("Invalid Current Password", "Error")
	
	if error is None:
		base_app.db.session.commit()
	
	return render_template('user/update_user.html', error = error, user = current_user)
	
