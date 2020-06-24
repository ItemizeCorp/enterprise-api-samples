import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
 
url = 'https://sandbox.proapi.itemize.com/api/enterprise/v1/accounts/<ACCOUNT ID HERE>/documents'
metadata = '{"format": "image/jpeg", "client_id": "123456", "client_country_id": 3}'

multipart_data = MultipartEncoder(fields={
	'document': ('boston_pizza.jpg', open('boston_pizza.jpg', 'rb'), 'image/jpeg'),
    'metadata': metadata
    })

print(multipart_data)

response = requests.post(
	url, 
	data=multipart_data,
	headers={'Content-Type': multipart_data.content_type},
	auth=('', '<API TOKEN HERE>'))
  
print(response.content)
