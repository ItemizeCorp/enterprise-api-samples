import unirest
import json
import os
import shutil
import argparse
import re
import uuid
from urllib import urlretrieve

accountId=<PASTE ACCOUNT ID HERE>
apiToken=<PASTE API TOKEN HERE>

def uploadDocument(metadataParams, filePath):
	response = unirest.post("%s%s/documents" % (url, accountId), 
	  params=
	  {
	  "metadata": metadataParams,
	  "document": open(filePath, 'rb')
	  }, 
	  auth=('', apiToken))

	print "%s,%s" % (filePath, response.raw_body)
	return response.code == 200


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = True, help = "List of GUIDs to upload")
ap.add_argument("-c", "--country", required = False, help = "country of upload: 1=us, 2=uk, 3=ca, 4=nz, 6=au", default=1)
args = vars(ap.parse_args())

url = "https://sandbox.proapi.itemize.com/api/enterprise/v1/accounts/"
is_digital = False

with open(args['file']) as f:
	lines = f.read().splitlines()

for line in lines:

	splits = line.split(",")
	if len(splits) > 1:
		from_address = splits[1]
		is_digital = True
	image = splits[0]

	
	if bool(re.search('.jpeg', image, re.I) or re.search('.jpg', image, re.I)):
		imageFormat = "image/jpeg" 
	elif bool(re.search('.png', image, re.I)):
		imageFormat = "image/png" 
	elif bool(re.search('.pdf', image, re.I)): 
		imageFormat = "application/pdf"
	elif bool(re.search('.html', image, re.I)): 
		imageFormat = "text/html"	
	else:
		imageFormat = "text/plain"

	if is_digital:
		uploadDocument(json.dumps({
			"format":imageFormat, 
			"from_address":from_address, 
			"client_id": str(uuid.uuid4()), 
			"client_country_id":int(args['country'])}), image)
	else:
		uploadDocument(json.dumps({
			"format":imageFormat, 
			"client_id":str(uuid.uuid4()),
			"client_country_id":int(args['country'])}), image)