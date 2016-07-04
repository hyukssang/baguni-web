from flask import *
from db import mysql
import parse
bagunis = Blueprint('bagunis', __name__, template_folder='templates')

@bagunis.route('/main/<user>/bagunis/<int:baguniid>', methods=['GET'])
def bagunis_route(user, baguniid):
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
		for db_item in db_items:
			if db_item[7] == 1:
				db_item[7] = 'checked'
			else:
				db_item[7] = ''
			item = {
				'origurl': db_item[2],
				'imageurl': db_item[3],
				'price': db_item[4],
				'brand': db_item[5],
				'name': db_item[6],
				'selected': db_item[7]
			}
			items.append(item)

		return render_template("bagunis.html", items = items)


api_addItem = Blueprint('api_addItem', __name__)

@api_addItem.route('/api/v1/addItem', methods=['POST'])
def api_addItem_route():
	if request.method == 'POST':
		jsondata = request.get_json()
		print jsondata['itemURL']
		return ('', 200)













