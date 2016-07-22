from flask import *
from db import mysql
from parselib import parseCafe24Mall

bagunis = Blueprint('bagunis', __name__, template_folder='templates')

@bagunis.route('/main/<user>/bagunis/<int:baguniid>', methods=['GET', 'POST'])
def bagunis_route(user, baguniid):
	# Check if a user is logged in
	# If not, redirect to the main page for login
	if 'email' not in session:
		print 'Not logged in: redirecting to main...'
		return redirect(url_for('main.main_route'))

	# Check if the url is the right url for the current user
	session_username = session['email'].split('@')[0]
	if session_username != user:
		return render_template('403.html'), 403

	# Check if the current Baguni is displayed to the right user
	curBaguniid = baguniid

	query_getEmail = 'SELECT email FROM BaguniAccess WHERE baguniid = %s'
	data_getEmail = [curBaguniid]

	conn = mysql.get_db()
	cursor = conn.cursor()
	cursor.execute(query_getEmail, data_getEmail)

	try:
		db_email = cursor.fetchall()[0][0]
		if db_email != session['email']:
			return render_template('403.html'), 403
	except IndexError:
		return render_template('403.html'), 403


	if request.method == 'GET':
		# Get info about items in the current Baguni from the database
		query_getItems = 'SELECT * FROM Item WHERE baguniid = %s ORDER BY itemname ASC'
		data_getItems = [curBaguniid]

		conn = mysql.get_db()
		cursor = conn.cursor()
		cursor.execute(query_getItems, data_getItems)
		db_items = cursor.fetchall()

		items = []
		checked = ''
		for db_item in db_items:
			if db_item[7] == 1:
				checked = 'checked'

			item = {
				'origurl': db_item[2],
				'imageurl': db_item[3],
				'price': db_item[4],
				'brand': db_item[5],
				'name': db_item[6],
				'selected': checked
			}
			items.append(item)

		return render_template("bagunis.html", items = items)
	if request.method == 'POST':
		# Receive json object from ajax request
		jsondata = request.get_json()
		itemURL = jsondata['itemURL']
		curStep = jsondata['step']

		print curStep

		if curStep == 0:
			# Parse the url given
			parseResult = parseCafe24Mall(itemURL)
			# {
			# 	'domain': domain,
			# 	'img': img,
			# 	'name': name,
			# 	'price': price,
			# 	'info': info
			# }

			parseSuccess = parseResult[0]
			parseError = parseResult[1]
			parseInfo = parseResult[2]
			print parseError
			print parseInfo
			
			return jsonify(
				errorMessage = parseError,
				checkImage = parseInfo['img'],
				checkBrand = parseInfo['domain'],
				checkName = parseInfo['name'],
				checkPrice = parseInfo['price'],
				moreInfo = parseInfo['info']
			)
		elif curStep == 1:
			print jsondata['price']
			print jsondata['moreInfo']
			query_addItem = ('INSERT INTO Item(baguniid, originalurl, imageurl, price, '
							 'brandname, itemname, addInfo) VALUES (%s,%s,%s,%s,%s,%s,%s)')
			data_addItem = [baguniid, itemURL, jsondata['imageURL'], jsondata['price'], jsondata['brandName'],
							jsondata['itemName'], jsondata['moreInfo']]

			conn = mysql.get_db()
			cursor = conn.cursor()
			cursor.execute(query_addItem, data_addItem)
			conn.commit()

		return ('', 200)
