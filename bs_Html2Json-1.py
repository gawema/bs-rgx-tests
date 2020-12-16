import pprint
import htmlmin
from bs4 import BeautifulSoup, ResultSet, element as Element

def convetToJson(el=None, newjson={}):
	if type(el) == Element.Tag:
		print('tag')
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
	
	pprint.pprint(jComponents)
