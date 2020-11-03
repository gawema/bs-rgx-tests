
from bs4 import BeautifulSoup
import re

def get_childrens(parent_element):
	child_elements = parent_element.findAll(True, recursive=False)
	print(child_elements)
	print("----------------------------------------------")
	if(len(child_elements)==0):
		return child_elements
	for child in child_elements:
		get_childrens(child)
	return child_elements

with open("index.html",'r') as f:
	soup = BeautifulSoup(f.read(), "html.parser")
	first_layer_elements = soup.findAll(re.compile(r"editable-\w*[ \n a-z=\'\"]*"))
	print(first_layer_elements)
	print("--------------------------------------------- child_elements")
	for element in first_layer_elements:
		print(element)
		child_elements = element.findAll(True, recursive=False)==