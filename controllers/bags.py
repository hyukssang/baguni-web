from flask import *

bags = Blueprint('bags', __name__, template_folder='templates')

@bags.route('/bags')
def bags_route():
	
	return render_template("bags.html")

api_AddBags = Blueprint('api_AddBags', __name__, template_folder='templates')

@api_AddBags.route('/api/v1/AddBags', methods=['GET', 'POST'])
def api_AddBags_route():
	
	return render_template("bags.html")