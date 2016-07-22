# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
from urlparse import urlparse
import re
import sys
import requests
# reload(sys)
# sys.setdefaultencoding('utf-8')

def parseCafe24Mall(url):
	itemInfo = {
		"domain": "",
		"img": "",
		"name": "",
		"price": "",
		"info": {}
	}
	errorMsg = ''
	# Retrieve html document to be parsed
	domain = urlparse(url).netloc.split('.')

	html = ''
	if 'm' in domain:
		url = re.sub("m.", "", url, count = 1)

	print url
	html = urllib.urlopen(url).read()

	if domain[-2] == 'co':		# co.kr
		domain = domain[-3]
	else:
		domain = domain[-2]
	
	# Init BeautifulSoup
	soup = BeautifulSoup(html, 'html.parser')

	# Image url
	try:
		img = soup.find_all('img','BigImage')[0]['src']
	except:
		try:
			img = soup.find_all('img', 'bigImage')[0]['src']
		except:
			try:
				img = soup.find_all('img', 'Bigimage')[0]['src']
			except:
				try:
					img = soup.find_all('img', 'bigimage')[0]['src']
				except:
					errorMsg = 'Image parsing failed.'
					return (False, errorMsg, itemInfo)

	# Name of the item
	try:
		name = soup.select('tr td span')[0].get_text()
		if not name:
			name = soup.select('.detailArea h3')[0].get_text()
	except:
		errorMsg = 'Name parsing failed.'
		return (False, errorMsg, itemInfo)
	# Price (Reflects sale price if it exists)
	try:
		if soup.select('#span_product_price_sale'):
			print 'sale price exists'
			price = soup.select('#span_product_price_sale')[0].find(text=True, recursive=False)
		else:
			print 'not on sale'
			price = soup.select('#span_product_price_text')[0].find(text=True, recursive=False)
		print price
		price = re.sub("[^0-9]", "", price)
	except:
		errorMsg = 'Price parsing failed.'
		return (False, errorMsg, itemInfo)

	# Size, Color
	try:
		info = {}
		selects = soup.select('.ProductOption0')
		for i in range(0, len(selects)):
			options = soup.select('#product_option_id'+str(i+1)+' option')
			ops = []
			for j in range(2, len(options)):
				ops.append(options[j].string)
			info[selects[i]['option_title']] = ops
	except:
		errorMsg = 'Info parsing failed.'
		return (False, errorMsg, itemInfo)

	print "Domain: " + domain
	print "Image URL: " + img
	print "Name: " + name
	print "Price: " + price
	print "Info: "
	print info

	itemInfo['domain'] = domain
	itemInfo['img'] = img
	itemInfo['name'] = name
	itemInfo['price'] = price
	itemInfo['info'] = info

	return (True, errorMsg, itemInfo)
