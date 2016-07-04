from flask import *
from db import mysql
import encrypt

signup = Blueprint('signup', __name__, template_folder='templates')

@signup.route('/signup', methods=['GET', 'POST'])
def signup_route():
	if request.method == 'GET':
		print 'SignUp GET'
		return render_template('signup.html')

	elif request.method == 'POST':
		print 'SignUp POST'

		f = request.form

		# Create a new User
		if checkIfEmailExists(f['email']):
			salt = encrypt.genSalt()
			newPassword = encrypt.encryptPassword(salt, f['password'])

			query_AddUser = 'INSERT INTO User VALUES (%s,%s,%s,%s,%s)'
			data_AddUser = [f['firstname'], f['lastname'], newPassword, f['email'], f['phone']]
			
			conn = mysql.get_db()
			cursor = conn.cursor()
			cursor.execute(query_AddUser, data_AddUser)
			conn.commit()

			return render_template('bagunis.html')
		else:
			error = 'Email already exists'
			return render_template('signup.html', error = error)

# Function to check if provided email already exists in the db
def checkIfEmailExists(email):
	print 'checkIfEmailExists'
	query_GetEmail = 'SELECT * FROM User WHERE email = %s'
	data_GetEmail = [email]

	conn = mysql.get_db()
	cursor = conn.cursor()
	cursor.execute(query_GetEmail, data_GetEmail)
	result = cursor.fetchall()
	print len(result)
	if len(result) == 0:
		return True
	return False


