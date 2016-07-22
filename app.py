from flask import Flask
from db import *

import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder="templates")

app.register_blueprint(controllers.main)
app.register_blueprint(controllers.main_user)
app.register_blueprint(controllers.login)
app.register_blueprint(controllers.signup)
app.register_blueprint(controllers.bagunis)

app.register_blueprint(controllers.api_parse)
# app.register_blueprint(controllers.api_addBaguni)
# app.register_blueprint(controllers.api_addItem)

app.config.from_object(TestingConfig)
mysql.init_app(app)

app.secret_key = 'never_reveal'

# Run the app on a local development server
if __name__=='__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)