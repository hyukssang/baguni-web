from flask import *

insideBags = Blueprint('insideBags', __name__, template_folder='templates')

@insideBags.route('/insideBags')
def insideBags_route():
	return render_template("insideBags.html")