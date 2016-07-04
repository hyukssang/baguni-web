from flask import *
from db import mysql

main = Blueprint('main', __name__, template_folder = 'templates')

@main.route('/main')
def main_route():
	return render_template('main.html')

main_user = Blueprint('main_user', __name__, template_folder='templates')

@main_user.route('/main/<user>', methods=['GET'])
def main_user_route(user):
	# Check if the url is the right url for the current user
	session_username = session['email'].split('@')[0]
	if session_username != user:
		return render_template('403.html'), 403

	# Check if a user is logged in
	# If not, redirect to the main page for login
	if 'email' not in session:
		print 'Not logged in: redirecting to main...'
		return redirect(url_for('main.main_route'))

	if request.method == 'GET':
		print 'baguni GET'
		# Get all the Baguni IDs associated with the email account
		query_getBaguniId = 'SELECT * FROM BaguniAccess WHERE email = %s'
		data_getBaguniId = [session['email']]

		conn = mysql.get_db()
		cursor = conn.cursor()
		cursor.execute(query_getBaguniId, data_getBaguniId)
		baguniid = cursor.fetchall()

		bagunis = []

		for i in range(0, len(baguniid)):
			curBaguniId = baguniid[i][1]
			# For each Baguni ID, get Baguni info
			query_getBaguni = 'SELECT * FROM Baguni WHERE baguniid = %s'
			data_getBaguni = [curBaguniId]

			cursor.execute(query_getBaguni, data_getBaguni)
			baguni = cursor.fetchall()[0]

			# For each Baguni, count the number of items in that Baguni
			query_getNumItems = 'SELECT COUNT(itemid) FROM Item WHERE baguniid = %s'
			data_getNumItems = [curBaguniId]

			cursor.execute(query_getNumItems, data_getNumItems)
			numItems = cursor.fetchall()[0][0]

			# For each Baguni, count the number of items SELECTED in that Baguni
			query_getNumSelected = 'SELECT COUNT(itemid) FROM Item WHERE baguniid = %s AND selected = %s'
			data_getNumSelected = [curBaguniId, 1]

			cursor.execute(query_getNumSelected, data_getNumSelected)
			numSelected = cursor.fetchall()[0][0]


			newBaguni = [baguni, numItems, numSelected]
			
			bagunis.append(newBaguni)

		return render_template("main_user.html", bagunis = bagunis, user = user)

api_addBaguni = Blueprint('api_addBaguni', __name__)

@api_addBaguni.route('/api/v1/addBaguni', methods=['POST'])
def api_addBaguni_route():
	if request.method == 'POST':
		print 'baguni POST'
		jsondata = request.get_json()
		baguniName = jsondata['baguniName']
		baguniColor = jsondata['baguniColor']

		# Insert into Baguni
		query_addBaguni = 'INSERT INTO Baguni (email, title, color) VALUES (%s, %s, %s)'
		data_addBaguni = [session['email'], baguniName, baguniColor]

		conn = mysql.get_db()
		cursor = conn.cursor()
		cursor.execute(query_addBaguni, data_addBaguni)
		conn.commit()

		# Get the id of inserted Baguni
		query_getBaguniId = 'SELECT LAST_INSERT_ID()'
		
		baguniid = cursor.execute(query_getBaguniId)
		baguniid = cursor.fetchall()[0]

		# Insert into BaguniAccess the newly added Baguni
		query_addBagAccess = 'INSERT INTO BaguniAccess (email, baguniid) VALUES (%s, %s)'
		data_addBagAccess = [session['email'], baguniid]

		cursor.execute(query_addBagAccess, data_addBagAccess)
		conn.commit()

		return ('', 200)
		# return render_template("baguni.html")
















