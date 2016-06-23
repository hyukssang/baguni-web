from flask import *

baguni = Blueprint('baguni', __name__, template_folder='templates')

@baguni.route('/baguni')
def baguni_route():
	
	return render_template("baguni.html")

api_addBaguni = Blueprint('api_addBaguni', __name__, template_folder='templates')

@api_addBaguni.route('/api/v1/addBaguni', methods=['GET', 'POST'])
def api_addBaguni_route():
	
	return render_template("baguni.html")