from flask import *

insideBaguni = Blueprint('insideBaguni', __name__, template_folder='templates')

@insideBaguni.route('/insideBaguni')
def insideBaguni_route():
	return render_template("insideBaguni.html")