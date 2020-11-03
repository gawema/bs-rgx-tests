import sys
import getopt

inputfile = ''
outputfile = 'clea'

def get_args(argv):
	global inputfile
	global outputfile
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

def main(argv):
	get_args(argv)
	if inputfile:
		try:
			with open(inputfile, 'r') as file:	
				html = file.read()
				print(html)
		except:
			print('not a valid input')

	else:
		print('no input file given')
		


if __name__ == "__main__":
	main(sys.argv[1:])
	