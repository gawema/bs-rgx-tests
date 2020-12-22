import re
from bs4 import BeautifulSoup, ResultSet,element as Element
import json
import boto3

s3 = boto3.resource('s3')
bucket_name = "cms-test-buckett"


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

def lambda_handler(event, context):
  sComponents = []
  user = event['user']
  project = event['project']
  file = event['file']
  components = event['pages'][0]['components']
	
  for component in components:
  	sComponent = convertToHtml(component, '')
  	sComponents.append(sComponent)

  obj = s3.Object('cms-test-buckett', user+'/'+project+'/'+file)
  body = obj.get()['Body'].read()
  
  soup = BeautifulSoup(body, "html.parser")
  
  for i, component in enumerate(soup.findAll("editable")):
  	soup = re.sub(str(component), str(sComponents[i]), str(soup), 1)
  	
  s3_file_path = user + '/' + project + '/' + file
  
  s3.Bucket(bucket_name).put_object(Key=s3_file_path, Body=soup)
  file_object = s3.Bucket(bucket_name).Object(s3_file_path)
  file_object.Acl().put(ACL = 'public-read')
  
  return {
	    'statusCode': 200,
	  	'body': 'https://'+ bucket_name +'.s3.eu-central-1.amazonaws.com/'+s3_file_path
	}
	