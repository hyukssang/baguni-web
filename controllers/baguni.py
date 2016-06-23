from flask import *
from db import mysql

baguni = Blueprint('baguni', __name__, template_folder='templates')

@baguni.route('/baguni')
def baguni_route():
	
	return render_template("baguni.html")

api_addBaguni = Blueprint('api_addBaguni', __name__, template_folder='templates')

@api_addBaguni.route('/api/v1/addBaguni', methods=['POST'])
def api_addBaguni_route():
	# To test if ajax call made it to this place
	print '/api/v1/addBaguni'

	return render_template("baguni.html")