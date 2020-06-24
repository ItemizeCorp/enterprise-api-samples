import unirest
import json

# Out of the box:  pass your account_id and API Token as parameters for each method.

# For JSON data params, use the json.dumps() method.
# Example: updateAccount(accountId, apiToken, json.dumps({"email_address":"newEmail@gmail.com"}))
# Example: uploadDocument(accountId, apiToken, json.dumps({"format":"image/jpeg"}), "/receipts/sample-receipt.jpeg")

url="https://sandbox.proapi.itemize.com/api/enterprise/v1/accounts/"

def getAccount(accountId, apiToken):
	response = unirest.get("%s%s" % (url, accountId), auth=('', apiToken))
	print response.raw_body

def updateAccount(accountId, apiToken, dataParams):
	response = unirest.put("%s%s" % (url, accountId), 
		headers={"Content-Type":"application/json"}, 
		params=dataParams, 
		auth=('', apiToken))
	print response.raw_body

def uploadDocument(accountId, apiToken, metadataParams, filePath):
	response = unirest.post("%s%s/documents" % (url, accountId), 
	  params=
	  {
	  "metadata":metadataParams,
	  "document": open(filePath, 'rb')
	  }, 
	  auth=('', apiToken))

	print response.raw_body

def getDocument(accountId, apiToken, docId):
	response = unirest.get("%s%s/documents/%s" % (url, accountId, docId), auth=('', apiToken))
	print response.raw_body

def addWebhook(accountId, apiToken, dataParams):
	response = unirest.post("%s%s/webhooks" % (url, accountId),
		headers={"Content-Type":"application/json"},
		params=dataParams,
		auth=('', apiToken))
	print response.raw_body

def updateWebhook(accountId, apiToken, webhookId, dataParams):
	response = unirest.put("%s%s/webhooks/%s" % (url, accountId, webhookId),
		headers={"Content-Type":"application/json"},
		params=dataParams,
		auth=('', apiToken))
	print response.raw_body


def getWebhooks(accountId, apiToken):
	response = unirest.get("%s%s/webhooks" % (url, accountId), auth=('', apiToken))
	print response.raw_body

def getWebhook(accountId, apiToken, webhookId):
	response = unirest.get("%s%s/webhooks/%s" % (url, accountId, webhookId), auth=('', apiToken))
	print response.raw_body

def deleteWebhook(accountId, apiToken, webhookId):
	response = unirest.delete("%s%s/webhooks/%s" % (url, accountId, webhookId), auth=('', apiToken))
	print response.raw_body