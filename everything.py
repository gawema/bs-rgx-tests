import pprint
import re
import htmlmin
from bs4 import BeautifulSoup, ResultSet,element as Element
import uuid

def convetToJson(el=None,json={}):
	if type(el) == Element.Tag:
		json[el.name] = {'attributes': el.attrs}
		json[el.name] = convetToJson(el.contents,json[el.name])
		return json[el.name]
	elif len(el):
		elements = []
		text = ''
		for el in el:
			if type(el) == Element.Tag:
				value = convetToJson(el,json)
				elements.append({el.name:value})
			else:
				text += el.strip()
		json['text'] = text
		return json
	else:
		return json

def convertToHtml(json, a):
	for k in json:
		a += '<' + k + ' '
		# add attributes
		el = json.get(k)
		if "attributes" in el:
			attrs = el.get('attributes')
			for attr in attrs:
				a += attr + '="' + attrs[attr] + '" '
			el.pop("attributes")
		a += '>'
		if "text" in el:
			text = el.get('text')
			a += text
			el.pop("text")
		if len(el) > 0:
			a = convertToHtml(el, a)
		a += "</"+k+">"
	return a

def recunstructHTMLfile(soup, jComponents):
	# file = str(soup)
	with open("output.html", "r") as file:
		soup = BeautifulSoup(file.read(), "html.parser")

		for i, component in enumerate(soup.findAll("editable-paragraph")):

			newComponent = next(item for item in jComponents if item['editable-paragraph']['attributes']["cms_id"] == component.attrs['cms_id'])			
			print(newComponent.get('editable-paragraph').get('attributes'))
			quit()
			
			oldComponent = str(component)
			match = re.search(oldComponent, file).group()
			if match:
				newcontent = re.sub(match, "newString", file)
				file = newcontent
		with open('index2.html', 'x') as file:
			file.write(newcontent)

			# updateComponent = component.replace("prova")
			# updateComponent = Tag(newComponent.K)
			# component.replace_with(updateComponent)

with open("index.html",'r') as file:
	html = file.read()
	minified_html=htmlmin.minify(html)

	soup = BeautifulSoup(minified_html, "html.parser")

	components = soup.findAll("editable-paragraph")
	jComponents = []
	jComponent = {}
	for component in components:
		uniqueId = uuid.uuid4().hex
		component.attrs['cms_id'] = uniqueId
		jComponent[component.name] = convetToJson(component)
		jComponents.append(jComponent.copy())
	
	with open("output.html", "w") as file:
		file.write(str(soup.prettify()))
		file.close()
	
	## test editing
	jComponents[0]['editable-paragraph']['text'] = "ciao"

	recunstructHTMLfile(soup ,jComponents)

	file.close()

	# print("--------------------JSON--------------------")	
	# # pprint.pprint(jComponents)
	# print("--------------------HTML--------------------")	
	# for jComponent in jComponents:
		# pprint.pprint(convertToHtml(jComponent, ''))
	
	