import pprint
import re
import htmlmin
from bs4 import BeautifulSoup, ResultSet,element as Element
import uuid


def convetToJson(el=None, newjson={}):
	if type(el) == Element.Tag:
		newjson = {
			'name': el.name,
			'attributes': el.attrs,
			'child_components': []
		}
		for child in el.contents:
			if type(child) == Element.Tag:
				childComponent = convetToJson(child, newjson)
				newjson['child_components'].append(childComponent)
			else:
				newjson['text'] = child
		return newjson

def convertToHtml(json, element):
	element += '<' + json['name']
	for attr in json['attributes']:
		element += " " + attr + '="' +  json['attributes'][attr] + '"'
	element += '>' + json['text']
	if len(json['child_components']) > 0:
		for child in json['child_components']:
			element = convertToHtml(child, element)
	element += '</'+ json['name'] + ">"
	return element	




sComponents = []
sComponent = {}

with open("index.html",'r') as file:
	html = file.read()
	minified_html=htmlmin.minify(html)

	soup = BeautifulSoup(minified_html, "html.parser")

	components = soup.findAll("editable")
	jComponents = []
	jComponent = {}
	for component in components:
		jComponent = convetToJson(component)
		jComponents.append(jComponent.copy())

	jComponents[0]['text'] = "FUNZIONAA"
	jComponents[1]['text'] = "FINALMENTE"

	print(jComponents)
	for jComponent in jComponents:
		sComponent = convertToHtml(jComponent, '')
		sComponents.append(sComponent)

	file.close()

with open("index.html", "r") as file2:
	# print(sComponents)
	soup = BeautifulSoup(file2.read(), "html.parser")
	for i, component in enumerate(soup.findAll("editable")):
		soup = re.sub(str(component), str(sComponents[i]), str(soup), 1)
		print(soup)
	with open('index2.html', 'w') as file:
		file.write(str(soup))

	
	