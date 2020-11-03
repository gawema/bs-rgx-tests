import re

start_regex = r"<editable-\w*[ \n a-z=''""]*>"
middle_regex = r"[a-zA-Z0-9_<>/ \n]+"
end_regex = r"</editable-\w*>"

with open('index.html', 'r') as f:
    originalFile = f.read()

# finds all editable components
matches = re.findall(start_regex + middle_regex + end_regex, originalFile)
if matches:
	for match in matches:
		# storing the component & its name
		component = re.search(start_regex, match).group().rsplit('>')[0]
		componentName = component.rsplit(' ')[0][1:]
		has_inner_components = re.findall( r"<\w*[ \n a-z=''""]*>[a-zA-Z0-9_<>/ \n]*</\w*>", match)
		print(has_inner_components)

		# asking to edit the componet
		print('found', componentName)
		edit = input("Do you whant to edit this? (Y) ")

		if edit == 'Y':
			# asking for new content
			newString = component + ">" + input("Enter new value: ") + "</" + componentName + ">"
			newcontent = re.sub(match, newString, originalFile)

			# updating originalFile
			originalFile = newcontent

			# replacing file with new content
			with open('index.html', 'w') as file:
				file.write(newcontent)
		else:
			pass
else:
	print('did not find any components')

f.close()

## this test does not regognize childerens of component so it replaces everithing