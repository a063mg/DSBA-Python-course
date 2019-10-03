import urllib
import requests
from lxml import html

import json

pas = True

url = input("url: ")
output = input("output file: ")
try:
	page_html = urllib.request.urlopen(url).read()
except Exception as e:
	print("Wrong url:")
	print (e)
	pas = False

if pas:
	links = []

	parsed_page = html.fromstring(page_html)
	for div_element in parsed_page.xpath("//a"):
		try:
			link = div_element.get("href")
			if link != None:
				if link[0:8] == "https://":
					text = div_element.text
					links.append((text, link))
		except Exception as e:
			print("Ooops")
			print (e)
			pas = False

	if pas:
		json.dump(links, open(output, "w+"))

#restored = json.load(open("links.json"))


#https://en.wikipedia.org/wiki/Recursion