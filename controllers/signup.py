from flask import *
from db import mysql

signup = Blueprint('signup', __name__, template_folder='templates')

@signup.route('/signup', methods=['GET', 'POST'])
def signup_route():
	if request.method == 'GET':
		print 'SignUp GET'
		return render_template('signup.html')
	elif request.method == 'POST':
		print 'SignUp POST'

		f = request.form
		
		query_AddUser = 'INSERT INTO User VALUES (%s,%s,%s,%s,%s)'
		data_AddUser = [f['firstname'], f['lastname'], f['password'], f['email'], f['phone']]
		
		conn = mysql.get_db()
		cursor = conn.cursor()
		cursor.execute(query_AddUser, data_AddUser)
		conn.commit()

		return render_template('baguni.html')