from flask import Flask

import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder="templates")

app.register_blueprint(controllers.bags)
app.register_blueprint(controllers.insideBags)

app.register_blueprint(controllers.api_AddBags)

app.secret_key = 'never_reveal'

# Run the app on a local development server
if __name__=='__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)