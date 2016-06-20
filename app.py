from flask import Flask

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder="templates")

# Run the app on a local development server
if __name__=='__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)