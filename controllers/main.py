from flask import *

main = Blueprint('main', __name__, template_folder = 'templates')

@main.route('/main')
def main_route():
	return render_template('index.html')