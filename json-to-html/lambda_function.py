import re
from bs4 import BeautifulSoup, ResultSet,element as Element

project = {
  "last_update": "2020-12-21T16:35:58.829Z",
  "pages": [
    {
      "components": [
        {
          "child_components": [
            {
              "_id": "5fe0ceee47b91400099a4bb2",
              "name": "div",
              "child_components": [
                {
                  "_id": "5fe0ceee47b91400099a4bb3",
                  "name": "h1",
                  "child_components": [],
                  "text": "world"
                }
              ],
              "text": "hello"
            }
          ],
          "_id": "5fe0ceee47b91400099a4bb1",
          "name": "editable",
          "attributes": {
            "val": "1, 3"
          },
          "text": "ciao"
        },
        {
          "child_components": [
            {
              "_id": "5fe0ceee47b91400099a4bb5",
              "name": "div",
              "child_components": [
                {
                  "_id": "5fe0ceee47b91400099a4bb6",
                  "name": "h1",
                  "child_components": [],
                  "text": "world"
                }
              ],
              "text": "hello"
            }
          ],
          "_id": "5fe0ceee47b91400099a4bb4",
          "name": "editable",
          "attributes": {
            "val": "1, 3"
          },
          "text": "ciao"
        }
      ],
      "_id": "5fe0ceec25892616637b0511",
      "name": "index.html"
    }
  ],
  "_id": "5fe0ceec25892616637b0510",
  "name": "index.html"
}
jComponents = project['pages'][0]['components']
sComponents = []

def convertToHtml(json, element):
	element += '<' + json['name']
	if hasattr(json, 'attributes'):
		for attr in json['attributes']:
			element += " " + attr + '="' +  json['attributes'][attr] + '"'
	element += '>' + json['text']
	if len(json['child_components']) > 0:
		for child in json['child_components']:
			element = convertToHtml(child, element)
	element += '</'+ json['name'] + ">"
	return element	

for jComponent in jComponents:
	sComponent = convertToHtml(jComponent, '')
	sComponents.append(sComponent)

with open("index.html", "r") as file2:
	soup = BeautifulSoup(file2.read(), "html.parser")
	for i, component in enumerate(soup.findAll("editable")):
		soup = re.sub(str(component), str(sComponents[i]), str(soup), 1)
	with open('index2.html', 'w') as file:
		file.write(str(soup))

	
	