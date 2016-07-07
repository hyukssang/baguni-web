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
	# Retrieve html document to be parsed
	html = urllib.urlopen(url).read()
	domain = urlparse(url).netloc.split('.')
	if domain[-2] == 'co':		# co.kr
		domain = domain[-3]
	else:
		domain = domain[-2]

	# Init BeautifulSoup
	soup = BeautifulSoup(html, 'html.parser')

	img = soup.find_all('img','BigImage')[0]['src']

	# Image url
	img = soup.find_all('img','BigImage')[0]['src']
	# Name of the item
	name = soup.select('tr td span')[0].get_text()
	if not name:
		name = soup.select('.detailArea h3')[0].get_text()
	# Price (Reflects sale price if it exists)
	if soup.select('#span_product_price_sale'):
		print 'sale price exists'
		price = soup.select('#span_product_price_sale')[0].find(text=True, recursive=False)
	else:
		print 'not on sale'
		price = soup.select('#span_product_price_text')[0].find(text=True, recursive=False)
	print price
	price = re.sub("[^0-9]", "", price)

	# Size, Color
	info = {}
	selects = soup.select('.ProductOption0')
	for i in range(0, len(selects)):
		options = soup.select('#product_option_id'+str(i+1)+' option')
		ops = []
		for j in range(2, len(options)):
			ops.append(options[j].string)
		info[selects[i]['option_title']] = ops

	print "Domain: " + domain
	print "Image URL: " + img
	print "Name: " + name
	print "Price: " + price
	print "Info: "
	print info

	return {
		'domain': domain,
		'img': img,
		'name': name,
		'price': price,
		'info': info
	}







