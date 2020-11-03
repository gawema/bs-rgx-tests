import pprint
import htmlmin
from bs4 import BeautifulSoup, ResultSet, element as Element

def convetToJson(el=None, json={}):
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

with open("index.html",'r') as file:
	html = file.read()
	minified_html=htmlmin.minify(html)
	soup = BeautifulSoup(minified_html, "html.parser")
	components = soup.findAll("editable-paragraph")
	jComponents = []
	jComponent = {}
	for component in components:
		jComponent[component.name] = convetToJson(component)
		jComponents.append(jComponent.copy())
	
	pprint.pprint(jComponents)
