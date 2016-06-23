from flask import *

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login')
def login_route():
	return render_template('login.html')