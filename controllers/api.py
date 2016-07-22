from flask import *
from db import mysql
from parselib import parseCafe24Mall

api_parse = Blueprint('api_parse', __name__)

@api_parse.route('/api/v1/parse', methods=['POST'])
def api_parse_route():
	if request.method == 'POST':
		print "/api/v1/parse"

		# Receive json object from mobile request
		jsondata = request.get_json()
		print jsondata

		# Parse the url given
		parseResult = parseCafe24Mall(jsondata['currentURL'])
		parseSuccess = parseResult[0]
		parseError = parseResult[1]
		parseInfo = parseResult[2]
		print "parseError: " + parseError
		print parseInfo
		return jsonify(
			errorMessage = parseError,
			checkImage = parseInfo['img'],
			checkBrand = parseInfo['domain'],
			checkName = parseInfo['name'],
			checkPrice = parseInfo['price'],
			moreInfo = parseInfo['info']
		)
