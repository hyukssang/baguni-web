from flask import *
from db import mysql
import encrypt

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['GET', 'POST'])
def login_route():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		f = request.form

		query_GetUser = 'SELECT * FROM User WHERE email = %s'
		data_GetUser = [f['email']]
		
		conn = mysql.get_db()
		cursor = conn.cursor()
		cursor.execute(query_GetUser, data_GetUser)
		result = cursor.fetchall()
		error = ''

		# If a user does not exist
		if not result:
			error = 'Email does not exist'
		# If password does not match
		else:
			# Get the existing salt
			dbSalt = result[0][2].split('$')[1]
			dbPassword = result[0][2]

			formPassword = encrypt.encryptPassword(dbSalt, f['password'])
			
			if formPassword != dbPassword:
				error = 'Wrong password'
			else:
				session['email'] = f['email']
				session['name'] = result[0][0] + ' ' + result[0][1]
				user = f['email'].split('@')[0]
				return redirect(url_for('main_user.main_user_route', user=user))
		
		return render_template('login.html', error = error)





