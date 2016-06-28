from flask import *
from db import mysql

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
		else:
			# If password does not match
			if f['password'] != result[0][2]:
				error = 'Wrong password'
			else:
				return render_template('baguni.html')
		
		return render_template('login.html', error = error)